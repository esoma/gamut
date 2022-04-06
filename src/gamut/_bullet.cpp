
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// stdlib
#include <vector>
// bullet
#define BT_USE_DOUBLE_PRECISION
#include "btBulletDynamicsCommon.h"
#include "BulletCollision/CollisionDispatch/btInternalEdgeUtility.h"
#include "BulletCollision/CollisionShapes/btTriangleShape.h"
#include "BulletCollision/CollisionShapes/btHeightfieldTerrainShape.h"
#include "BulletCollision/NarrowPhaseCollision/btRaycastCallback.h"
#include <iostream>
// glm
#include <glm/glm.hpp>
// gamut
#include "gamut/math.h"

#define ASSERT(x) if (!(x)){ std::cout << "ASSERTION FAILURE: " << __FILE__ << ":" << __LINE__ << std::endl; exit(1); }


extern ContactAddedCallback gContactAddedCallback;


glm::dvec3
GamutCalculateTrimeshNormal(
    btBvhTriangleMeshShape* trimesh,
    const glm::dvec3 *normals,
    const glm::dvec3& point,
    int part_id,
    int triangle_index
)
{
    const auto mesh_interface = (btTriangleIndexVertexArray *)trimesh->getMeshInterface();
    const auto& mesh_array = mesh_interface->getIndexedMeshArray();
    const auto& mesh = mesh_array[part_id];
    const int *indices = (const int *)mesh.m_triangleIndexBase;
    const int *tri_indexes = &indices[triangle_index * 3];
    auto *positions = (const glm::dvec3 *)mesh.m_vertexBase;

    auto *position_0 = &positions[tri_indexes[0]];
    auto *position_1 = &positions[tri_indexes[1]];
    auto *position_2 = &positions[tri_indexes[2]];

    auto *normal_0 = &normals[tri_indexes[0]];
    auto *normal_1 = &normals[tri_indexes[1]];
    auto *normal_2 = &normals[tri_indexes[2]];

    // https://en.wikipedia.org/wiki/Point-normal_triangle
    // https://blog.demofox.org/2019/12/07/bezier-triangles/
    auto b300 = *position_0;
    auto b030 = *position_1;
    auto b003 = *position_2;
    #define P(i) (positions[i - 1])
    #define N(i) (normals[i - 1])
    #define w(i, j) (glm::dot(P(j) - P(i), N(i)))
    auto b012 = (1 / 3.0) * (2.0 * P(3) + P(2) - w(3, 2) * N(3));
    auto b021 = (1 / 3.0) * (2.0 * P(2) + P(3) - w(2, 3) * N(2));
    auto b102 = (1 / 3.0) * (2.0 * P(3) + P(1) - w(3, 1) * N(3));
    auto b201 = (1 / 3.0) * (2.0 * P(1) + P(3) - w(1, 3) * N(1));
    auto b120 = (1 / 3.0) * (2.0 * P(2) + P(1) - w(2, 1) * N(2));
    auto b210 = (1 / 3.0) * (2.0 * P(1) + P(2) - w(1, 2) * N(1));
    auto E = (1 / 6.0) * (b012 + b021 + b102 + b201 + b120 + b210);
    auto V = (1 / 3.0) * (P(1) + P(2) + P(3));
    auto b111 = E + .5 * (E - V);

    // interpolate the "real" (smoothed) normal for the intersection point
    // barycentric
    auto v0 = b030 - b300;
    auto v1 = b003 - b300;
    auto v2 = point - b300;
    auto d00 = glm::dot(v0, v0);
    auto d01 = glm::dot(v0, v1);
    auto d11 = glm::dot(v1, v1);
    auto d20 = glm::dot(v2, v0);
    auto d21 = glm::dot(v2, v1);
    auto denom = d00 * d11 - d01 * d01;
    auto v = (d11 * d20 - d01 * d21) / denom;
    auto w = (d00 * d21 - d01 * d20) / denom;
    auto u = 1.0 - v - w;

    return glm::normalize(
        (*normal_0) * u +
        (*normal_1) * v +
        (*normal_2) * w
    );
}


bool
GamutContactAddedCallback(
    btManifoldPoint& cp,
    const btCollisionObjectWrapper* colObj1Wrap,
    int partId1,
    int index1,
    const btCollisionObjectWrapper* colObj0Wrap,
    int partId0,
    int index0
)
{
    // this is similar to btAdjustInternalEdgeContacts, except we use real
    // normal data to correct the normals so that tri meshes do not have
    // "bumpy" behavior

	if (colObj0Wrap->getCollisionShape()->getShapeType() != TRIANGLE_SHAPE_PROXYTYPE)
    {
		return true;
    }

	auto trimesh = (btBvhTriangleMeshShape*)colObj0Wrap->getCollisionObject()->getCollisionShape();
    auto *normals = (const glm::dvec3 *)trimesh->getUserPointer();
    if (!normals){ return true; }
    auto final_normal = GamutCalculateTrimeshNormal(
        trimesh,
        normals,
        glm::dvec3(cp.m_localPointB[0], cp.m_localPointB[1], cp.m_localPointB[2]),
        partId0,
        index0
    );

    // correct the normal and reproject the collision point along it
    cp.m_normalWorldOnB = btVector3(
        final_normal.x,
        final_normal.y,
        final_normal.z
    );
    cp.m_positionWorldOnB = cp.m_positionWorldOnA - cp.m_normalWorldOnB * cp.m_distance1;
    cp.m_localPointB = colObj0Wrap->getWorldTransform().invXform(cp.m_positionWorldOnB);
    return true;
}


// Python Structures
// ----------------------------------------------------------------------------


struct ModuleState
{
    struct GamutMathApi *math_api;
};


struct World
{
    PyObject_HEAD
    btDefaultCollisionConfiguration *collision_config;
    btCollisionDispatcher *collision_dispatcher;
    btDbvtBroadphase *broadphase;
    btSequentialImpulseConstraintSolver *solver;
    btDiscreteDynamicsWorld *world;
};


struct Shape
{
    PyObject_HEAD
    // the Shape only owns this if is_compound is set, note that we still do
    // not own the sub-shapes -- in either case they should be held by a
    // wrapper object using the capsules returned by the shape adding methods
    btCollisionShape *shape;
    // indicates that shape is a btCompoundShape
    bool is_compound;
    // indicates that this shape only works with static bodies
    bool must_be_static;
    // all the trimeshes that exist in the compound shape (only if the shape is
    // compound, if only composed of a single trimesh this will be empty)
    //
    // the Shape does not own these, they are again held externally by the
    // wrapper using capsules
    std::vector<btBvhTriangleMeshShape*> trimesh_shapes;
};


struct Body
{
    PyObject_HEAD
    // no reference held -- the wrapper should hold the only reference to this
    // object
    PyObject *wrapper;
    // Body has ownership of these
    btDefaultMotionState *motion_state;
    btRigidBody *body;
    // no reference held -- the shape itself must be maintained externally by
    // the wrapper
    Shape *shape;
    // Body has ownership of these
    std::vector<btRigidBody*> trimesh_bodies;
    // no reference held -- this relationship is maintained by the World
    World* world;
};


static ModuleState *get_module_state();


// World
// ----------------------------------------------------------------------------


static PyObject *
World___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {NULL};
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "", kwlist
    )){ return 0; }

    World *self = (World*)cls->tp_alloc(cls, 0);

    self->collision_config = new btDefaultCollisionConfiguration();
    self->collision_dispatcher = new btCollisionDispatcher(
        self->collision_config
    );
    self->broadphase = new btDbvtBroadphase();
    self->solver = new btSequentialImpulseConstraintSolver;
    self->world = new btDiscreteDynamicsWorld(
        self->collision_dispatcher,
        self->broadphase,
        self->solver,
        self->collision_config
    );
    self->world->setGravity(btVector3(0, 0, 0));

    return (PyObject *)self;
}


static void
World___dealloc__(World *self)
{
    const auto& bt_bodies = self->world->getCollisionObjectArray();
    for (int i = 0; i < bt_bodies.size(); i++)
    {
        auto bt_body = bt_bodies[i];
        auto body = (Body *)bt_body->getUserPointer();
        // note that multiple bt bodies may share the same Body, so we may have
        // already set the world to 0 for the same Body
        ASSERT(body->world == self || body->world == 0);
        body->world = 0;
    }

    delete self->world;
    delete self->solver;
    delete self->broadphase;
    delete self->collision_dispatcher;
    delete self->collision_config;

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef World_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyObject *
World_add_body(World *self, PyObject *args)
{
    Body *body = 0;
    int groups, mask;
    if (!PyArg_ParseTuple(args, "Oii", &body, &groups, &mask)){ return 0; }
    ASSERT(body->world == 0);
    self->world->addRigidBody(body->body, groups, mask);
    for (
        auto iter = body->trimesh_bodies.begin();
        iter != body->trimesh_bodies.end();
        ++iter
    )
    {
        self->world->addRigidBody((*iter), groups, mask);
    }
    body->world = self;
    Py_RETURN_NONE;
}


static PyObject *
World_remove_body(World *self, Body *body)
{
    ASSERT(body->world == self);
    body->world = 0;
    self->world->removeRigidBody(body->body);
    for (
        auto iter = body->trimesh_bodies.begin();
        iter != body->trimesh_bodies.end();
        ++iter
    )
    {
        self->world->removeRigidBody((*iter));
    }
    Py_RETURN_NONE;
}


static PyObject *
World_simulate(World *self, PyObject *args)
{
    ASSERT(self->world);

    auto state = get_module_state();
    double time;
    bool get_collisions;

    if (!PyArg_ParseTuple(args, "dp", &time, &get_collisions)){ return 0; }

    Py_BEGIN_ALLOW_THREADS;
    self->world->stepSimulation(time, 0);
    Py_END_ALLOW_THREADS;

    if (!get_collisions){ Py_RETURN_NONE; }

    int manifold_count = self->collision_dispatcher->getNumManifolds();
    PyObject *collisions = PyList_New(0);
    for (int i = 0; i < manifold_count; i++)
    {
        auto manifold =
            self->collision_dispatcher->getManifoldByIndexInternal(i);
        if (manifold->getNumContacts() == 0){ continue; }
        PyObject *contacts = PyList_New(manifold->getNumContacts());
        if (!contacts){ goto error; }
        Body *body_a = (Body*)manifold->getBody0()->getUserPointer();
        Body *body_b = (Body*)manifold->getBody1()->getUserPointer();
        PyObject *collision = PyTuple_Pack(
            3,
            body_a->wrapper,
            body_b->wrapper,
            contacts
        );
        PyList_Append(collisions, collision);
        Py_DECREF(collision);

        for (int j = 0; j < manifold->getNumContacts(); j++)
        {
            const auto& point = manifold->getContactPoint(j);
            PyObject *contact = PyTuple_New(5);
            if (!contact){ goto error; }
            PyList_SET_ITEM(contacts, j, contact);
            auto local_position_a = state->math_api->DVector3_Create(
                point.m_localPointA.m_floats
            );
            if (!local_position_a){ goto error; }
            PyTuple_SET_ITEM(contact, 0, local_position_a);
            auto world_position_a = state->math_api->DVector3_Create(
                point.m_positionWorldOnA.m_floats
            );
            if (!world_position_a){ goto error; }
            PyTuple_SET_ITEM(contact, 1, world_position_a);
            auto local_position_b = state->math_api->DVector3_Create(
                point.m_localPointB.m_floats
            );
            if (!local_position_b){ goto error; }
            PyTuple_SET_ITEM(contact, 2, local_position_b);
            auto world_position_b = state->math_api->DVector3_Create(
                point.m_positionWorldOnB.m_floats
            );
            if (!world_position_b){ goto error; }
            PyTuple_SET_ITEM(contact, 3, world_position_b);
            auto normal_b = state->math_api->DVector3_Create(
                point.m_normalWorldOnB.m_floats
            );
            if (!normal_b){ goto error; }
            PyTuple_SET_ITEM(contact, 4, normal_b);
        }
    }

    return collisions;
error:
    Py_XDECREF(collisions);
    return 0;
}


static PyObject *
World_raycast(World *self, PyObject *const *args, Py_ssize_t nargs)
{
    auto state = get_module_state();
    double *raw_from = state->math_api->DVector3_GetValuePointer(args[0]);
    double *raw_to = state->math_api->DVector3_GetValuePointer(args[1]);
    btVector3 from(raw_from[0], raw_from[1], raw_from[2]);
    btVector3 to(raw_to[0], raw_to[1], raw_to[2]);
    int groups = PyLong_AsLong(args[2]);
    int mask = PyLong_AsLong(args[3]);

    btCollisionWorld::ClosestRayResultCallback results(from, to);
    results.m_collisionFilterGroup = groups;
    results.m_collisionFilterMask = mask;

    self->world->rayTest(from, to, results);
    if (!results.hasHit())
    {
        Py_RETURN_NONE;
    }

    PyObject *hit = PyTuple_New(4);

    PyObject *position = state->math_api->DVector3_Create(results.m_hitPointWorld.m_floats);
    if (!position){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 0, position);

    PyObject *normal = state->math_api->DVector3_Create(results.m_hitNormalWorld.m_floats);
    if (!normal){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 1, normal);

    Body *body = (Body*)results.m_collisionObject->getUserPointer();
    PyTuple_SET_ITEM(hit, 2, body->wrapper);
    Py_INCREF(body->wrapper);

    PyObject *fraction = PyFloat_FromDouble(results.m_closestHitFraction);
    if (PyErr_Occurred()){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 3, fraction);

    return hit;
}


static PyObject *
World_spherecast(World *self, PyObject *const *args, Py_ssize_t nargs)
{
    auto state = get_module_state();
    double *raw_from = state->math_api->DVector3_GetValuePointer(args[0]);
    double *raw_to = state->math_api->DVector3_GetValuePointer(args[1]);
    btVector3 from(raw_from[0], raw_from[1], raw_from[2]);
    btVector3 to(raw_to[0], raw_to[1], raw_to[2]);
    int groups = PyLong_AsLong(args[2]);
    int mask = PyLong_AsLong(args[3]);
    double radius = PyFloat_AsDouble(args[4]);

    btSphereShape sphere(radius);

    btCollisionWorld::ClosestConvexResultCallback results(from, to);
    results.m_collisionFilterGroup = groups;
    results.m_collisionFilterMask = mask;

    btTransform from_t;
    from_t.setIdentity();
    from_t.setOrigin(from);
    btTransform to_t;
    to_t.setIdentity();
    to_t.setOrigin(to);
    self->world->convexSweepTest(&sphere, from_t, to_t, results);
    if (!results.hasHit())
    {
        Py_RETURN_NONE;
    }

    PyObject *hit = PyTuple_New(4);

    PyObject *position = state->math_api->DVector3_Create(results.m_hitPointWorld.m_floats);
    if (!position){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 0, position);

    PyObject *normal = state->math_api->DVector3_Create(results.m_hitNormalWorld.m_floats);
    if (!normal){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 1, normal);

    Body *body = (Body*)results.m_hitCollisionObject->getUserPointer();
    PyTuple_SET_ITEM(hit, 2, body->wrapper);
    Py_INCREF(body->wrapper);

    PyObject *fraction = PyFloat_FromDouble(results.m_closestHitFraction);
    if (PyErr_Occurred()){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 3, fraction);

    return hit;
}


static PyMethodDef World_PyMethodDef[] = {
    {"add_body", (PyCFunction)World_add_body, METH_O, 0},
    {"remove_body", (PyCFunction)World_remove_body, METH_O, 0},
    {"simulate", (PyCFunction)World_simulate, METH_O, 0},
    {"raycast", (PyCFunction)World_raycast, METH_FASTCALL, 0},
    {"spherecast", (PyCFunction)World_spherecast, METH_FASTCALL, 0},
    {0, 0, 0, 0}
};


static PyObject *
World_Getter_gravity(World *self, void *)
{
    auto state = get_module_state();
    auto gravity = self->world->getGravity();
    return state->math_api->DVector3_Create(gravity.m_floats);
}


int
World_Setter_gravity(World *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *gravity = state->math_api->DVector3_GetValuePointer(value);
    if (!gravity){ return -1; }
    self->world->setGravity(btVector3(gravity[0], gravity[1], gravity[2]));
    return 0;
}


static PyGetSetDef World_PyGetSetDef[] = {
    {
        "gravity",
        (getter)World_Getter_gravity,
        (setter)World_Setter_gravity,
        0,
        0
    },
    {0, 0, 0, 0, 0}
};


static PyType_Slot World_PyType_Slots [] = {
    {Py_tp_new, (void*)World___new__},
    {Py_tp_dealloc, (void*)World___dealloc__},
    {Py_tp_members, (void*)World_PyMemberDef},
    {Py_tp_methods, (void*)World_PyMethodDef},
    {Py_tp_getset, (void*)World_PyGetSetDef},
    {0, 0},
};


static PyType_Spec World_PyTypeSpec = {
    "gamut.physics._physics.World",
    sizeof(World),
    0,
    Py_TPFLAGS_DEFAULT,
    World_PyType_Slots
};


static PyTypeObject *
define_world_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &World_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "World", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


// Body
// ----------------------------------------------------------------------------


void
Body_shape_update(Body *self, int groups, int mask)
{
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        if (self->world)
        {
            self->world->world->removeRigidBody(*iter);
        }
        delete (*iter)->getMotionState();
        delete *iter;
    }
    self->trimesh_bodies.clear();

    for (
        auto iter = self->shape->trimesh_shapes.begin();
        iter != self->shape->trimesh_shapes.end();
        ++iter
    )
    {
        btRigidBody::btRigidBodyConstructionInfo info(
            0,
            new btDefaultMotionState(btTransform::getIdentity()),
            *iter,
            btVector3(0, 0, 0)
        );
        info.m_friction = self->body->getFriction();
        info.m_restitution = self->body->getRestitution();
        info.m_startWorldTransform = self->body->getWorldTransform();

        auto body = new btRigidBody(info);
        body->setUserPointer(self);
        body->setCollisionFlags(
            btCollisionObject::CF_STATIC_OBJECT |
            btCollisionObject::CF_CUSTOM_MATERIAL_CALLBACK
        );
        if (self->world)
        {
            self->world->world->addRigidBody(body, groups, mask);
        }

        self->trimesh_bodies.push_back(body);
    }
}


static PyObject *
Body___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    PyObject *wrapper = 0;
    double mass = 0;
    Shape *shape = 0;

    static char *kwlist[] = {
        "wrapper",
        "mass",
        "shape",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "OdO", kwlist,
        &wrapper,
        &mass,
        &shape
    )){ return 0; }

    Body *self = (Body*)cls->tp_alloc(cls, 0);

    self->motion_state = new btDefaultMotionState(btTransform::getIdentity());
    btVector3 local_inertia;
    shape->shape->calculateLocalInertia(mass, local_inertia);
    btRigidBody::btRigidBodyConstructionInfo info(
        mass,
        self->motion_state,
        shape->shape,
        local_inertia
    );
    info.m_friction = 0;

    self->wrapper = wrapper;
    self->body = new btRigidBody(info);
    self->shape = shape;
    self->world = 0;

    self->body->setUserPointer(self);
    self->body->setCollisionFlags(btCollisionObject::CF_CUSTOM_MATERIAL_CALLBACK);
    // since the body isn't associated with a world yet we can pass in 0 for
    // the groups and mask
    Body_shape_update(self, 0, 0);

    return (PyObject *)self;
}


static void
Body___dealloc__(Body *self)
{
    if (self->world)
    {
        self->world->world->removeRigidBody(self->body);
    }
    delete self->body;
    delete self->motion_state;
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        if (self->world)
        {
            self->world->world->removeRigidBody(*iter);
        }
        delete (*iter)->getMotionState();
        delete *iter;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef Body_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyObject *
Body_set_mass(Body *self, PyObject *args)
{
    double mass = PyFloat_AsDouble(args);
    if (PyErr_Occurred()){ return 0; }

    btVector3 local_inertia;
    self->shape->shape->calculateLocalInertia(mass, local_inertia);
    self->body->setMassProps(mass, local_inertia);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_can_sleep(Body *self, PyObject *)
{
    self->body->setActivationState(ACTIVE_TAG);
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        (*iter)->setActivationState(ACTIVE_TAG);
    }
    Py_RETURN_NONE;
}


static PyObject *
Body_set_cannot_sleep(Body *self, PyObject *)
{
    self->body->setActivationState(DISABLE_DEACTIVATION);
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        (*iter)->setActivationState(DISABLE_DEACTIVATION);
    }
    Py_RETURN_NONE;
}


static PyObject *
Body_set_gravity(Body *self, PyObject *args, void *)
{
    bool is_explicit;
    PyObject *value;
    if (!PyArg_ParseTuple(args, "bO",
        &is_explicit, &value)){ return 0; }

    auto state = get_module_state();
    double *gravity = state->math_api->DVector3_GetValuePointer(value);
    if (!gravity){ return 0; }

    if (is_explicit)
    {
        self->body->setFlags(BT_DISABLE_WORLD_GRAVITY);
    }
    else
    {
        self->body->setFlags(0);
    }
    self->body->setGravity(btVector3(gravity[0], gravity[1], gravity[2]));
    Py_RETURN_NONE;
}


static PyObject *
Body_set_shape(Body *self, PyObject *const *args, Py_ssize_t nargs)
{
    ASSERT(nargs == 3);
    Shape *shape = (Shape *)args[0];
    int groups = PyLong_AsLong(args[1]);
    int mask = PyLong_AsLong(args[2]);
    if (
        shape->must_be_static &&
        !(self->body->getCollisionFlags() & btCollisionObject::CF_STATIC_OBJECT)
    )
    {
        return PyErr_Format(PyExc_ValueError, "this shape cannot be applied to a non-static body");
    }
    self->shape = shape;
    self->body->setCollisionShape(shape->shape);
    Body_shape_update(self, groups, mask);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_to_dynamic(Body *self, PyObject *)
{
    if (self->shape->must_be_static)
    {
        return PyErr_Format(PyExc_ValueError, "body composed of a shape that must be static");
    }
    auto flags = self->body->getCollisionFlags();
    flags &= ~btCollisionObject::CF_KINEMATIC_OBJECT;
    flags &= ~btCollisionObject::CF_STATIC_OBJECT;
    self->body->setCollisionFlags(flags);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_to_kinematic(Body *self, PyObject *)
{
    if (self->shape->must_be_static)
    {
        return PyErr_Format(PyExc_ValueError, "body composed of a shape that must be static");
    }
    auto flags = self->body->getCollisionFlags();
    flags |= btCollisionObject::CF_KINEMATIC_OBJECT;
    flags &= ~btCollisionObject::CF_STATIC_OBJECT;
    self->body->setCollisionFlags(flags);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_to_static(Body *self, PyObject *)
{
    auto flags = self->body->getCollisionFlags();
    flags &= ~btCollisionObject::CF_KINEMATIC_OBJECT;
    flags |= btCollisionObject::CF_STATIC_OBJECT;
    self->body->setCollisionFlags(flags);
    self->body->setAngularVelocity(btVector3(0, 0, 0));
    self->body->setLinearVelocity(btVector3(0, 0, 0));
    Py_RETURN_NONE;
}


static PyObject *
Body_wake(Body *self, PyObject *)
{
    self->body->activate();
    Py_RETURN_NONE;
}


static PyMethodDef Body_PyMethodDef[] = {
    {
        "set_mass",
        (PyCFunction)Body_set_mass,
        METH_O,
        0
    },
    {
        "set_can_sleep",
        (PyCFunction)Body_set_can_sleep,
        METH_NOARGS,
        0
    },
    {
        "set_cannot_sleep",
        (PyCFunction)Body_set_cannot_sleep,
        METH_NOARGS,
        0
    },
    {
        "set_gravity",
        (PyCFunction)Body_set_gravity,
        METH_O,
        0
    },
    {
        "set_shape",
        (PyCFunction)Body_set_shape,
        METH_FASTCALL,
        0
    },
    {
        "set_to_dynamic",
        (PyCFunction)Body_set_to_dynamic,
        METH_NOARGS,
        0
    },
    {
        "set_to_kinematic",
        (PyCFunction)Body_set_to_kinematic,
        METH_NOARGS,
        0
    },
    {
        "set_to_static",
        (PyCFunction)Body_set_to_static,
        METH_NOARGS,
        0
    },
    {
        "wake",
        (PyCFunction)Body_wake,
        METH_NOARGS,
        0
    },
    {0, 0, 0, 0}
};


static PyObject *
Body_Getter_angular_damping(Body *self, void *)
{
    btScalar damping = self->body->getAngularDamping();
    return PyFloat_FromDouble(damping);
}


static int
Body_Setter_angular_damping(Body *self, PyObject *value, void *)
{
    double damping = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setDamping(self->body->getLinearDamping(), damping);
    return 0;
}


static PyObject *
Body_Getter_angular_freedom(Body *self, void *)
{
    auto state = get_module_state();
    const auto& angular_factor = self->body->getAngularFactor();
    bool xyz[3] = {
        angular_factor[0] != 0,
        angular_factor[1] != 0,
        angular_factor[2] != 0
    };
    return state->math_api->BVector3_Create(xyz);
}


static int
Body_Setter_angular_freedom(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    bool *angular_freedom = state->math_api->BVector3_GetValuePointer(value);
    if (!angular_freedom){ return -1; }
    btVector3 angular_factor(
        angular_freedom[0] ? 1 : 0,
        angular_freedom[1] ? 1 : 0,
        angular_freedom[2] ? 1 : 0
    );
    self->body->setAngularFactor(angular_factor);
    const auto &velocity = self->body->getAngularVelocity();
    self->body->setAngularVelocity(velocity * angular_factor);
    return 0;
}


static PyObject *
Body_Getter_angular_sleep_threshold(Body *self, void *)
{
    btScalar threshold = self->body->getAngularSleepingThreshold();
    return PyFloat_FromDouble(threshold);
}


static int
Body_Setter_angular_sleep_threshold(Body *self, PyObject *value, void *)
{
    double threshold = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setSleepingThresholds(
        self->body->getLinearSleepingThreshold(),
        threshold
    );
    return 0;
}


static PyObject *
Body_Getter_angular_velocity(Body *self, void *)
{
    auto state = get_module_state();
    const auto &velocity = self->body->getAngularVelocity();
    return state->math_api->DVector3_Create(velocity.m_floats);
}


static int
Body_Setter_angular_velocity(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *velocity = state->math_api->DVector3_GetValuePointer(value);
    if (!velocity){ return -1; }
    const auto& angular_factor = self->body->getAngularFactor();
    self->body->setAngularVelocity(
        btVector3(velocity[0], velocity[1], velocity[2]) *
        angular_factor
    );
    return 0;
}


static PyObject *
Body_Getter_friction(Body *self, void *)
{
    btScalar friction = self->body->getFriction();
    return PyFloat_FromDouble(friction);
}


static int
Body_Setter_friction(Body *self, PyObject *value, void *)
{
    double friction = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setFriction(friction);
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        (*iter)->setFriction(friction);
    }
    return 0;
}


static PyObject *
Body_Getter_is_sleeping(Body *self, void *)
{
    return PyBool_FromLong(!self->body->isActive());
}


static PyObject *
Body_Getter_linear_damping(Body *self, void *)
{
    btScalar damping = self->body->getLinearDamping();
    return PyFloat_FromDouble(damping);
}


static int
Body_Setter_linear_damping(Body *self, PyObject *value, void *)
{
    double damping = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setDamping(damping, self->body->getAngularDamping());
    return 0;
}


static PyObject *
Body_Getter_linear_freedom(Body *self, void *)
{
    auto state = get_module_state();
    const auto& linear_factor = self->body->getLinearFactor();
    bool xyz[3] = {
        linear_factor[0] != 0,
        linear_factor[1] != 0,
        linear_factor[2] != 0
    };
    return state->math_api->BVector3_Create(xyz);
}


static int
Body_Setter_linear_freedom(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    bool *linear_freedom = state->math_api->BVector3_GetValuePointer(value);
    if (!linear_freedom){ return -1; }
    btVector3 linear_factor(
        linear_freedom[0] ? 1 : 0,
        linear_freedom[1] ? 1 : 0,
        linear_freedom[2] ? 1 : 0
    );
    self->body->setLinearFactor(linear_factor);
    const auto &velocity = self->body->getAngularVelocity();
    self->body->setLinearVelocity(velocity * linear_factor);
    return 0;
}


static PyObject *
Body_Getter_linear_sleep_threshold(Body *self, void *)
{
    btScalar threshold = self->body->getLinearSleepingThreshold();
    return PyFloat_FromDouble(threshold);
}


static int
Body_Setter_linear_sleep_threshold(Body *self, PyObject *value, void *)
{
    double threshold = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setSleepingThresholds(
        threshold,
        self->body->getAngularSleepingThreshold()
    );
    return 0;
}


static PyObject *
Body_Getter_linear_velocity(Body *self, void *)
{
    auto state = get_module_state();
    const auto& velocity = self->body->getLinearVelocity();
    return state->math_api->DVector3_Create(velocity.m_floats);
}


static int
Body_Setter_linear_velocity(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *velocity = state->math_api->DVector3_GetValuePointer(value);
    if (!velocity){ return -1; }
    const auto& linear_factor = self->body->getLinearFactor();
    self->body->setLinearVelocity(
        btVector3(velocity[0], velocity[1], velocity[2]) *
        linear_factor
    );
    return 0;
}


static PyObject *
Body_Getter_rolling_friction(Body *self, void *)
{
    btScalar friction = self->body->getRollingFriction();
    return PyFloat_FromDouble(friction);
}


static int
Body_Setter_rolling_friction(Body *self, PyObject *value, void *)
{
    double friction = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setRollingFriction(friction);
    return 0;
}


static PyObject *
Body_Getter_restitution(Body *self, void *)
{
    btScalar restitution = self->body->getRestitution();
    return PyFloat_FromDouble(restitution);
}


static int
Body_Setter_restitution(Body *self, PyObject *value, void *)
{
    double restitution = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setRestitution(restitution);
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        (*iter)->setRestitution(restitution);
    }
    return 0;
}


static PyObject *
Body_Getter_spinning_friction(Body *self, void *)
{
    btScalar friction = self->body->getSpinningFriction();
    return PyFloat_FromDouble(friction);
}


static int
Body_Setter_spinning_friction(Body *self, PyObject *value, void *)
{
    double friction = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setSpinningFriction(friction);
    return 0;
}


static PyObject *
Body_Getter_tangible(Body *self, void *)
{
    return PyBool_FromLong((self->body->getCollisionFlags() & btCollisionObject::CF_NO_CONTACT_RESPONSE) == 0);
}


static int
Body_Setter_tangible(Body *self, PyObject *value, void *)
{
    auto flags = self->body->getCollisionFlags();
    if (value == Py_True)
    {
        flags &= ~btCollisionObject::CF_NO_CONTACT_RESPONSE;
    }
    else
    {
        flags |= btCollisionObject::CF_NO_CONTACT_RESPONSE;
    }
    self->body->setCollisionFlags(flags);
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        (*iter)->setCollisionFlags(flags);
    }
    return 0;
}


static PyObject *
Body_Getter_transform(Body *self, void *)
{
    auto state = get_module_state();
    btScalar matrix[16];
    btTransform transform = self->body->getWorldTransform();
    transform.getOpenGLMatrix(matrix);
    return state->math_api->DMatrix4x4_Create(matrix);
}


static int
Body_Setter_transform(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *matrix = state->math_api->DMatrix4x4_GetValuePointer(value);
    if (!matrix){ return -1; }

    btTransform transform;
    transform.setFromOpenGLMatrix(matrix);
    self->motion_state->setWorldTransform(transform);
    self->body->setWorldTransform(transform);
    for (
        auto iter = self->trimesh_bodies.begin();
        iter != self->trimesh_bodies.end();
        ++iter
    )
    {
        (*iter)->setWorldTransform(transform);
    }
    return 0;
}


static PyGetSetDef Body_PyGetSetDef[] = {
    {
        "angular_damping",
        (getter)Body_Getter_angular_damping,
        (setter)Body_Setter_angular_damping,
        0,
        0
    },
    {
        "angular_freedom",
        (getter)Body_Getter_angular_freedom,
        (setter)Body_Setter_angular_freedom,
        0,
        0
    },
    {
        "angular_sleep_threshold",
        (getter)Body_Getter_angular_sleep_threshold,
        (setter)Body_Setter_angular_sleep_threshold,
        0,
        0
    },
    {
        "angular_velocity",
        (getter)Body_Getter_angular_velocity,
        (setter)Body_Setter_angular_velocity,
        0,
        0
    },
    {
        "friction",
        (getter)Body_Getter_friction,
        (setter)Body_Setter_friction,
        0,
        0
    },
    { "is_sleeping", (getter)Body_Getter_is_sleeping, 0, 0, 0 },
    {
        "linear_damping",
        (getter)Body_Getter_linear_damping,
        (setter)Body_Setter_linear_damping,
        0,
        0
    },
    {
        "linear_freedom",
        (getter)Body_Getter_linear_freedom,
        (setter)Body_Setter_linear_freedom,
        0,
        0
    },
    {
        "linear_velocity",
        (getter)Body_Getter_linear_velocity,
        (setter)Body_Setter_linear_velocity,
        0,
        0
    },
    {
        "linear_sleep_threshold",
        (getter)Body_Getter_linear_sleep_threshold,
        (setter)Body_Setter_linear_sleep_threshold,
        0,
        0
    },
    {
        "rolling_friction",
        (getter)Body_Getter_rolling_friction,
        (setter)Body_Setter_rolling_friction,
        0,
        0
    },
    {
        "spinning_friction",
        (getter)Body_Getter_spinning_friction,
        (setter)Body_Setter_spinning_friction,
        0,
        0
    },
    {
        "restitution",
        (getter)Body_Getter_restitution,
        (setter)Body_Setter_restitution,
        0,
        0
    },
    {
        "tangible",
        (getter)Body_Getter_tangible,
        (setter)Body_Setter_tangible,
        0,
        0
    },
    {
        "transform",
        (getter)Body_Getter_transform,
        (setter)Body_Setter_transform,
        0,
        0
    },
    {0, 0, 0, 0, 0}
};


static PyType_Slot Body_PyType_Slots [] = {
    {Py_tp_new, (void*)Body___new__},
    {Py_tp_dealloc, (void*)Body___dealloc__},
    {Py_tp_members, (void*)Body_PyMemberDef},
    {Py_tp_methods, (void*)Body_PyMethodDef},
    {Py_tp_getset, (void*)Body_PyGetSetDef},
    {0, 0},
};


static PyType_Spec Body_PyTypeSpec = {
    "gamut.physics._physics.Body",
    sizeof(Body),
    0,
    Py_TPFLAGS_DEFAULT,
    Body_PyType_Slots
};


static PyTypeObject *
define_body_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &Body_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "Body", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


// Shape
// ----------------------------------------------------------------------------


static PyObject *
Shape___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    int is_compound;
    static char *kwlist[] = {
        "",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "p", kwlist,
        &is_compound
    )){ return 0; }

    Shape *self = (Shape*)cls->tp_alloc(cls, 0);
    self->is_compound = is_compound != 0;
    self->must_be_static = false;
    if (is_compound != 0)
    {
        self->shape = new btCompoundShape();
    }
    else
    {
        self->shape = 0;
    }

    return (PyObject *)self;
}


static void
Shape___dealloc__(Shape *self)
{
    if (self->is_compound)
    {
        delete self->shape;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef Shape_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static void
bvh_tri_mesh_capsule_destructor(PyObject *capsule)
{
    btBvhTriangleMeshShape *bvh_tri_mesh = (
        (btBvhTriangleMeshShape *)PyCapsule_GetPointer(capsule, 0)
    );
    auto mesh_interface = bvh_tri_mesh->getMeshInterface();
    delete bvh_tri_mesh;
    delete mesh_interface;
}


static void
box_capsule_destructor(PyObject *capsule)
{
    btBoxShape *box = (btBoxShape *)PyCapsule_GetPointer(capsule, 0);
    delete box;
}


static void
capsule_capsule_destructor(PyObject *capsule)
{
    btCapsuleShape *shape = (btCapsuleShape *)PyCapsule_GetPointer(
        capsule,
        0
    );
    delete shape;
}


static void
cone_capsule_destructor(PyObject *capsule)
{
    btConeShape *cone = (btConeShape *)PyCapsule_GetPointer(
        capsule,
        0
    );
    delete cone;
}


static void
convex_hull_capsule_destructor(PyObject *capsule)
{
    btConvexHullShape *convex_hull = (btConvexHullShape *)PyCapsule_GetPointer(
        capsule,
        0
    );
    delete convex_hull;
}


static void
cylinder_capsule_destructor(PyObject *capsule)
{
    btCylinderShape *cylinder = (btCylinderShape *)PyCapsule_GetPointer(
        capsule,
        0
    );
    delete cylinder;
}


static void
plane_capsule_destructor(PyObject *capsule)
{
    btStaticPlaneShape *plane = (btStaticPlaneShape *)PyCapsule_GetPointer(
        capsule,
        0
    );
    delete plane;
}


static void
sphere_capsule_destructor(PyObject *capsule)
{
    btSphereShape *sphere = (btSphereShape *)PyCapsule_GetPointer(capsule, 0);
    delete sphere;
}


static PyObject *
Shape_add_capsule(Shape *self, PyObject *args)
{
    double radius = 0;
    double height = 0;
    double center_x = 0;
    double center_y = 0;
    double center_z = 0;
    double rotation_w = 0;
    double rotation_x = 0;
    double rotation_y = 0;
    double rotation_z = 0;
    if (!PyArg_ParseTuple(
        args, "ddddddddd",
        &radius, &height,
        &center_x, &center_y, &center_z,
        &rotation_w, &rotation_x, &rotation_y, &rotation_z
    )){ return 0; }

    auto capsule = new btCapsuleShape(radius, height);
    if (
        self->is_compound ||
        center_x != 0 || center_y != 0 || center_z != 0 ||
        rotation_w != 1 || rotation_x != 0 || rotation_y != 0 || rotation_z != 0
    )
    {
        btTransform transform = btTransform::getIdentity();
        transform.setOrigin(btVector3(center_x, center_y, center_z));
        transform.setRotation(btQuaternion(
            rotation_x, rotation_y, rotation_z, rotation_w
        ));
        if (!self->is_compound)
        {
            ASSERT(self->shape == 0);
            self->is_compound = true;
            self->shape = new btCompoundShape;
        }
        ((btCompoundShape*)self->shape)->addChildShape(transform, capsule);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = capsule;
    }
    return PyCapsule_New(capsule, 0, capsule_capsule_destructor);
}


static PyObject *
Shape_add_cone(Shape *self, PyObject *args)
{
    double radius = 0;
    double height = 0;
    double center_x = 0;
    double center_y = 0;
    double center_z = 0;
    double rotation_w = 0;
    double rotation_x = 0;
    double rotation_y = 0;
    double rotation_z = 0;
    if (!PyArg_ParseTuple(
        args, "ddddddddd",
        &radius, &height,
        &center_x, &center_y, &center_z,
        &rotation_w, &rotation_x, &rotation_y, &rotation_z
    )){ return 0; }

    auto cone = new btConeShape(radius, height);
    if (
        self->is_compound ||
        center_x != 0 || center_y != 0 || center_z != 0 ||
        rotation_w != 1 || rotation_x != 0 || rotation_y != 0 || rotation_z != 0
    )
    {
        btTransform transform = btTransform::getIdentity();
        transform.setOrigin(btVector3(center_x, center_y, center_z));
        transform.setRotation(btQuaternion(
            rotation_x, rotation_y, rotation_z, rotation_w
        ));
        if (!self->is_compound)
        {
            ASSERT(self->shape == 0);
            self->is_compound = true;
            self->shape = new btCompoundShape;
        }
        ((btCompoundShape*)self->shape)->addChildShape(transform, cone);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = cone;
    }
    return PyCapsule_New(cone, 0, cone_capsule_destructor);
}


static PyObject *
Shape_add_convex_hull(Shape *self, PyObject *points)
{
    auto convex_hull_shape = new btConvexHullShape();

    size_t point_count = PyTuple_GET_SIZE(points);
    for (size_t i = 0; i < point_count; i++)
    {
        auto point = PyTuple_GET_ITEM(points, i);
        double x, y, z;
        if (!PyArg_ParseTuple(
            point, "ddd",
            &x, &y, &z
        )){ return 0; }
        convex_hull_shape->addPoint(btVector3(x, y, z), false);
    }
    convex_hull_shape->recalcLocalAabb();
    convex_hull_shape->optimizeConvexHull();

    if (self->is_compound)
    {
        ((btCompoundShape*)self->shape)->addChildShape(btTransform::getIdentity(), convex_hull_shape);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = convex_hull_shape;
    }

    return PyCapsule_New(convex_hull_shape, 0, convex_hull_capsule_destructor);
}


static PyObject *
Shape_add_cylinder(Shape *self, PyObject *args)
{
    double radius = 0;
    double height = 0;
    double center_x = 0;
    double center_y = 0;
    double center_z = 0;
    double rotation_w = 0;
    double rotation_x = 0;
    double rotation_y = 0;
    double rotation_z = 0;
    if (!PyArg_ParseTuple(
        args, "ddddddddd",
        &radius, &height,
        &center_x, &center_y, &center_z,
        &rotation_w, &rotation_x, &rotation_y, &rotation_z
    )){ return 0; }

    auto cylinder = new btCylinderShape(btVector3(radius, height * .5, radius));
    if (
        self->is_compound ||
        center_x != 0 || center_y != 0 || center_z != 0 ||
        rotation_w != 1 || rotation_x != 0 || rotation_y != 0 || rotation_z != 0
    )
    {
        btTransform transform = btTransform::getIdentity();
        transform.setOrigin(btVector3(center_x, center_y, center_z));
        transform.setRotation(btQuaternion(
            rotation_x, rotation_y, rotation_z, rotation_w
        ));
        if (!self->is_compound)
        {
            ASSERT(self->shape == 0);
            self->is_compound = true;
            self->shape = new btCompoundShape;
        }
        ((btCompoundShape*)self->shape)->addChildShape(transform, cylinder);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = cylinder;
    }
    return PyCapsule_New(cylinder, 0, cylinder_capsule_destructor);
}


static PyObject *
Shape_add_plane(Shape *self, PyObject *args)
{
    double distance = 0;
    double normal_x = 0;
    double normal_y = 0;
    double normal_z = 0;
    if (!PyArg_ParseTuple(
        args, "dddd",
        &distance,
        &normal_x, &normal_y, &normal_z
    )){ return 0; }

    auto plane = new btStaticPlaneShape(
        btVector3(normal_x, normal_y, normal_z),
        distance
    );
    if (self->is_compound)
    {
        ((btCompoundShape*)self->shape)->addChildShape(btTransform::getIdentity(), plane);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = plane;
    }
    return PyCapsule_New(plane, 0, plane_capsule_destructor);
}


static PyObject *
Shape_add_mesh(Shape *self, PyObject *args)
{
    int num_vertices;
    double *vertices = 0;
    int num_triangle_indices;
    int *triangle_indices = 0;
    double *normals = 0;
    if (!PyArg_ParseTuple(
        args, "iLiLL",
        &num_vertices, &vertices,
        &num_triangle_indices, &triangle_indices,
        &normals
    )){ return 0; }

    auto mesh_interface = new btTriangleIndexVertexArray(
        num_triangle_indices,
        triangle_indices,
        sizeof(int) * 3,
        num_vertices,
        vertices,
        sizeof(double) * 3
    );
    auto bvh_tri_mesh = new btBvhTriangleMeshShape(mesh_interface, true);
    bvh_tri_mesh->setUserPointer(normals);

    if (self->is_compound)
    {
        self->trimesh_shapes.push_back(bvh_tri_mesh);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = bvh_tri_mesh;
    }
    self->must_be_static = true;

    return PyCapsule_New(bvh_tri_mesh, 0, bvh_tri_mesh_capsule_destructor);
}


static PyObject *
Shape_add_rectangular_cuboid(Shape *self, PyObject *args)
{
    double center_x = 0;
    double center_y = 0;
    double center_z = 0;
    double dimensions_x = 0;
    double dimensions_y = 0;
    double dimensions_z = 0;
    double rotation_w = 0;
    double rotation_x = 0;
    double rotation_y = 0;
    double rotation_z = 0;
    if (!PyArg_ParseTuple(
        args, "dddddddddd",
        &center_x, &center_y, &center_z,
        &dimensions_x, &dimensions_y, &dimensions_z,
        &rotation_w, &rotation_x, &rotation_y, &rotation_z
    )){ return 0; }

    auto box = new btBoxShape(btVector3(
        dimensions_x * .5,
        dimensions_y * .5,
        dimensions_z * .5
    ));
    if (
        self->is_compound ||
        center_x != 0 || center_y != 0 || center_z != 0 ||
        rotation_w != 1 || rotation_x != 0 || rotation_y != 0 || rotation_z != 0
    )
    {
        btTransform transform = btTransform::getIdentity();
        transform.setOrigin(btVector3(center_x, center_y, center_z));
        transform.setRotation(btQuaternion(
            rotation_x, rotation_y, rotation_z, rotation_w
        ));
        if (!self->is_compound)
        {
            ASSERT(self->shape == 0);
            self->is_compound = true;
            self->shape = new btCompoundShape;
        }
        ((btCompoundShape*)self->shape)->addChildShape(transform, box);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = box;
    }
    return PyCapsule_New(box, 0, box_capsule_destructor);
}



static PyObject *
Shape_add_sphere(Shape *self, PyObject *args)
{
    double radius = 0;
    double center_x = 0;
    double center_y = 0;
    double center_z = 0;
    if (!PyArg_ParseTuple(
        args, "dddd",
        &radius,
        &center_x, &center_y, &center_z
    )){ return 0; }

    auto sphere = new btSphereShape(radius);
    if (
        self->is_compound ||
        center_x != 0 || center_y != 0 || center_z != 0
    )
    {
        btTransform transform = btTransform::getIdentity();
        transform.setOrigin(btVector3(center_x, center_y, center_z));
        if (!self->is_compound)
        {
            ASSERT(self->shape == 0);
            self->is_compound = true;
            self->shape = new btCompoundShape;
        }
        ((btCompoundShape*)self->shape)->addChildShape(transform, sphere);
    }
    else
    {
        ASSERT(self->shape == 0);
        self->shape = sphere;
    }
    return PyCapsule_New(sphere, 0, sphere_capsule_destructor);
}


static PyObject *
Shape_calculate_local_inertia(Shape *self, PyObject *args)
{
    double mass = PyFloat_AsDouble(args);
    if (PyErr_Occurred()){ return 0; }

    btVector3 inertia;
    self->shape->calculateLocalInertia(mass, inertia);

    return Py_BuildValue("ddd", inertia.x(), inertia.y(), inertia.z());
}


struct ShapeMeshRaycastTriangleCallback: public btTriangleRaycastCallback
{
    btBvhTriangleMeshShape *m_mesh;
    const glm::dvec3& m_from;
    const glm::dvec3& m_to;
    glm::dvec3 m_ray_normal;
    bool m_hit;
    glm::dvec3 m_hit_point;
    btScalar m_hit_fraction;
    glm::dvec3 m_hit_normal_local;
    int m_triangle_index;

    ShapeMeshRaycastTriangleCallback(
        btBvhTriangleMeshShape* mesh,
        const glm::dvec3& from,
        const glm::dvec3& to,
        const btVector3& bt_from,
        const btVector3& bt_to
    ):
        btTriangleRaycastCallback(bt_from, bt_to, 0),
        m_from(from),
        m_to(to),
        m_ray_normal(glm::normalize(from - to)),
        m_mesh(mesh),
        m_hit(false)
    {
    }

    btScalar reportHit(
        const btVector3& hit_normal_local,
        btScalar hit_fraction,
        int part_id,
        int triangle_index
    )
    {
        // hit is not ealier in the ray than the one currently recorded
        if (m_hit && hit_fraction > m_hit_fraction){ return 0; }

        auto hit_point = m_from + (hit_fraction * (m_to - m_from));

        auto *normals = (const glm::dvec3 *)m_mesh->getUserPointer();
        if (normals)
        {
            auto adjusted_normal = GamutCalculateTrimeshNormal(
                m_mesh,
                normals,
                hit_point,
                part_id,
                triangle_index
            );
            if (glm::dot(m_ray_normal, adjusted_normal) <= 0)
            {
                return 0;
            }
            m_hit_normal_local = adjusted_normal;
        }
        else
        {
            m_hit_normal_local = glm::dvec3(
                hit_normal_local.x(),
                hit_normal_local.y(),
                hit_normal_local.z()
            );
        }
        m_hit = true;
        m_hit_point = hit_point;
        m_hit_fraction = hit_fraction;
        m_triangle_index = triangle_index;
        return hit_fraction;
    }
};


static PyObject *
Shape_mesh_raycast(Shape *self, PyObject *const *args, Py_ssize_t nargs)
{
    ASSERT(nargs == 2);
    auto state = get_module_state();

    auto from = (glm::dvec3 *)state->math_api->DVector3_GetValuePointer(args[0]);
    auto to = (glm::dvec3 *)state->math_api->DVector3_GetValuePointer(args[1]);

    btVector3 bt_from(from->x, from->y, from->z);
    btVector3 bt_to(to->x, to->y, to->z);

    auto mesh = (btBvhTriangleMeshShape*)self->shape;
    ShapeMeshRaycastTriangleCallback result(mesh, *from, *to, bt_from, bt_to);
    mesh->performRaycast(&result, bt_from, bt_to);

    if (!result.m_hit)
    {
        Py_RETURN_NONE;
    }

    PyObject *hit = PyTuple_New(4);

    PyObject *position = state->math_api->DVector3_Create((double *)&result.m_hit_point);
    if (!position){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 0, position);

    PyObject *normal = state->math_api->DVector3_Create((double *)&result.m_hit_normal_local);
    if (!normal){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 1, normal);

    PyObject *triangle_index = PyLong_FromLong(result.m_triangle_index);
    PyTuple_SET_ITEM(hit, 2, triangle_index);

    PyObject *fraction = PyFloat_FromDouble(result.m_hit_fraction);
    if (PyErr_Occurred()){ Py_DECREF(hit); return 0; }
    PyTuple_SET_ITEM(hit, 3, fraction);

    return hit;
}


static PyMethodDef Shape_PyMethodDef[] = {
    {
        "add_capsule",
        (PyCFunction)Shape_add_capsule,
        METH_O,
        0
    },
    {
        "add_cone",
        (PyCFunction)Shape_add_cone,
        METH_O,
        0
    },
    {
        "add_convex_hull",
        (PyCFunction)Shape_add_convex_hull,
        METH_O,
        0
    },
    {
        "add_cylinder",
        (PyCFunction)Shape_add_cylinder,
        METH_O,
        0
    },
    {
        "add_plane",
        (PyCFunction)Shape_add_plane,
        METH_O,
        0
    },
    {
        "add_mesh",
        (PyCFunction)Shape_add_mesh,
        METH_O,
        0
    },
    {
        "add_rectangular_cuboid",
        (PyCFunction)Shape_add_rectangular_cuboid,
        METH_O,
        0
    },
    {
        "add_sphere",
        (PyCFunction)Shape_add_sphere,
        METH_O,
        0
    },
    {
        "calculate_local_inertia",
        (PyCFunction)Shape_calculate_local_inertia,
        METH_O,
        0
    },
    {
        "mesh_raycast",
        (PyCFunction)Shape_mesh_raycast,
        METH_FASTCALL,
        0
    },
    {0, 0, 0, 0}
};


static PyGetSetDef Shape_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};


static PyType_Slot Shape_PyType_Slots [] = {
    {Py_tp_new, (void*)Shape___new__},
    {Py_tp_dealloc, (void*)Shape___dealloc__},
    {Py_tp_members, (void*)Shape_PyMemberDef},
    {Py_tp_methods, (void*)Shape_PyMethodDef},
    {Py_tp_getset, (void*)Shape_PyGetSetDef},
    {0, 0},
};


static PyType_Spec Shape_PyTypeSpec = {
    "gamut.physics._physics.Shape",
    sizeof(Shape),
    0,
    Py_TPFLAGS_DEFAULT,
    Shape_PyType_Slots
};


static PyTypeObject *
define_shape_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &Shape_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "Shape", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


// module
// ----------------------------------------------------------------------------

static PyMethodDef module_methods[] = {
    {0, 0, 0, 0}
};


static void
module_free(void* self)
{
    GamutMathApi_Release();
}


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut._bullet",
    0,
    sizeof(struct ModuleState),
    module_methods,
    0,
    0,
    0,
    module_free
};


PyMODINIT_FUNC
PyInit__bullet()
{
    gContactAddedCallback = GamutContactAddedCallback;

    ModuleState *state = 0;
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    if (!module){ goto error; }

    if (PyState_AddModule(module, &module_PyModuleDef) == -1){ goto error; }
    state = (ModuleState *)PyModule_GetState(module);

    if (!define_world_type(module)){ goto error; }
    if (!define_body_type(module)){ goto error; }
    if (!define_shape_type(module)){ goto error; }

    state->math_api = GamutMathApi_Get();
    if (!state->math_api){ goto error; }

    return module;
error:
    Py_CLEAR(module);
    return 0;
}


static PyObject *
get_module()
{
    PyObject *module = PyState_FindModule(&module_PyModuleDef);
    if (!module)
    {
        return PyErr_Format(PyExc_RuntimeError, "physics module not ready");
    }
    return module;
}


static ModuleState *
get_module_state()
{
    PyObject *module = get_module();
    if (!module){ return 0; }
    return (ModuleState *)PyModule_GetState(module);
}

