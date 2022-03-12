
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// bullet
#define BT_USE_DOUBLE_PRECISION
#include "btBulletDynamicsCommon.h"
#include <iostream>
// gamut
#include "gamut/math.h"

#define ASSERT(x) if (!x){ std::cout << __FILE__ << ":" << __LINE__ << std::endl; exit(1); }


struct ModuleState
{
    struct GamutMathApi *api;
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
    btCompoundShape *shape;
};


struct Body
{
    PyObject_HEAD
    PyObject *wrapper;
    btDefaultMotionState *motion_state;
    btRigidBody *body;
    Shape *shape;
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
    self->world->addRigidBody(body->body, groups, mask);
    Py_RETURN_NONE;
}


static PyObject *
World_remove_body(World *self, Body *body)
{
    self->world->removeRigidBody(body->body);
    Py_RETURN_NONE;
}


static PyObject *
World_simulate(World *self, PyObject *args)
{
    ASSERT(self->world);

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
        if (!contacts)
        {
            Py_DECREF(collisions);
            return 0;
        }
        for (int j = 0; j < manifold->getNumContacts(); j++)
        {
            const auto& point = manifold->getContactPoint(j);
            PyObject *contact = Py_BuildValue(
                "(ddd)(ddd)(ddd)(ddd)(ddd)",
                point.m_localPointA.x(),
                point.m_localPointA.y(),
                point.m_localPointA.z(),
                point.m_positionWorldOnA.x(),
                point.m_positionWorldOnA.y(),
                point.m_positionWorldOnA.z(),
                point.m_localPointB.x(),
                point.m_localPointB.y(),
                point.m_localPointB.z(),
                point.m_positionWorldOnB.x(),
                point.m_positionWorldOnB.y(),
                point.m_positionWorldOnB.z(),
                point.m_normalWorldOnB.x(),
                point.m_normalWorldOnB.y(),
                point.m_normalWorldOnB.z()
            );
            PyList_SET_ITEM(contacts, j, contact);
        }
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
    }

    return collisions;
}


static PyMethodDef World_PyMethodDef[] = {
    {"add_body", (PyCFunction)World_add_body, METH_O, 0},
    {"remove_body", (PyCFunction)World_remove_body, METH_O, 0},
    {"simulate", (PyCFunction)World_simulate, METH_O, 0},
    {0, 0, 0, 0}
};


static PyObject *
World_Getter_gravity(World *self, void *)
{
    auto state = get_module_state();
    auto gravity = self->world->getGravity();
    return state->api->GamutMathDVector3_Create(gravity.m_floats);
}


int
World_Setter_gravity(World *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *gravity = state->api->GamutMathDVector3_GetValuePointer(value);
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

    self->body->setUserPointer(self);

    return (PyObject *)self;
}


static void
Body___dealloc__(Body *self)
{
    delete self->body;
    delete self->motion_state;

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
Body_set_enabled(Body *self, PyObject *)
{
    self->body->setActivationState(ACTIVE_TAG);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_cannot_sleep(Body *self, PyObject *)
{
    self->body->setActivationState(DISABLE_DEACTIVATION);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_disabled(Body *self, PyObject *)
{
    self->body->setActivationState(DISABLE_SIMULATION);
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
    double *gravity = state->api->GamutMathDVector3_GetValuePointer(value);
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
Body_set_shape(Body *self, Shape *shape)
{
    self->shape = shape;
    self->body->setCollisionShape(shape->shape);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_to_dynamic(Body *self, PyObject *)
{
    self->body->setCollisionFlags(0);
    Py_RETURN_NONE;
}


static PyObject *
Body_set_to_kinematic(Body *self, PyObject *)
{
    self->body->setCollisionFlags(btCollisionObject::CF_KINEMATIC_OBJECT);
    Py_RETURN_NONE;
}

static PyObject *
Body_set_to_static(Body *self, PyObject *)
{
    self->body->setCollisionFlags(btCollisionObject::CF_STATIC_OBJECT);
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
        "set_enabled",
        (PyCFunction)Body_set_enabled,
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
        "set_disabled",
        (PyCFunction)Body_set_disabled,
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
        METH_O,
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


int
Body_Setter_angular_damping(Body *self, PyObject *value, void *)
{
    double damping = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setDamping(self->body->getLinearDamping(), damping);
    return 0;
}


static PyObject *
Body_Getter_angular_sleep_threshold(Body *self, void *)
{
    btScalar threshold = self->body->getAngularSleepingThreshold();
    return PyFloat_FromDouble(threshold);
}


int
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
    auto velocity = self->body->getAngularVelocity();
    return state->api->GamutMathDVector3_Create(velocity.m_floats);
}


int
Body_Setter_angular_velocity(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *velocity = state->api->GamutMathDVector3_GetValuePointer(value);
    if (!velocity){ return -1; }
    self->body->setAngularVelocity(btVector3(velocity[0], velocity[1], velocity[2]));
    return 0;
}


static PyObject *
Body_Getter_friction(Body *self, void *)
{
    btScalar friction = self->body->getFriction();
    return PyFloat_FromDouble(friction);
}


int
Body_Setter_friction(Body *self, PyObject *value, void *)
{
    double friction = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setFriction(friction);
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


int
Body_Setter_linear_damping(Body *self, PyObject *value, void *)
{
    double damping = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setDamping(damping, self->body->getAngularDamping());
    return 0;
}


static PyObject *
Body_Getter_linear_sleep_threshold(Body *self, void *)
{
    btScalar threshold = self->body->getLinearSleepingThreshold();
    return PyFloat_FromDouble(threshold);
}


int
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
    auto velocity = self->body->getLinearVelocity();
    return state->api->GamutMathDVector3_Create(velocity.m_floats);
}


int
Body_Setter_linear_velocity(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *velocity = state->api->GamutMathDVector3_GetValuePointer(value);
    if (!velocity){ return -1; }
    self->body->setLinearVelocity(btVector3(velocity[0], velocity[1], velocity[2]));
    return 0;
}


static PyObject *
Body_Getter_rolling_friction(Body *self, void *)
{
    btScalar friction = self->body->getRollingFriction();
    return PyFloat_FromDouble(friction);
}


int
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


int
Body_Setter_restitution(Body *self, PyObject *value, void *)
{
    double restitution = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setRestitution(restitution);
    return 0;
}


static PyObject *
Body_Getter_spinning_friction(Body *self, void *)
{
    btScalar friction = self->body->getSpinningFriction();
    return PyFloat_FromDouble(friction);
}


int
Body_Setter_spinning_friction(Body *self, PyObject *value, void *)
{
    double friction = PyFloat_AsDouble(value);
    if (PyErr_Occurred()){ return 0; }
    self->body->setSpinningFriction(friction);
    return 0;
}


static PyObject *
Body_Getter_transform(Body *self, void *)
{
    auto state = get_module_state();
    btScalar matrix[16];
    btTransform transform = self->body->getWorldTransform();
    transform.getOpenGLMatrix(matrix);
    return state->api->GamutMathDMatrix4x4_Create(matrix);
}


int
Body_Setter_transform(Body *self, PyObject *value, void *)
{
    auto state = get_module_state();
    double *matrix = state->api->GamutMathDMatrix4x4_GetValuePointer(value);
    if (!matrix){ return -1; }

    btTransform transform;
    transform.setFromOpenGLMatrix(matrix);
    self->motion_state->setWorldTransform(transform);
    self->body->setWorldTransform(transform);
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
    static char *kwlist[] = {NULL};
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "", kwlist
    )){ return 0; }

    Shape *self = (Shape*)cls->tp_alloc(cls, 0);
    self->shape = new btCompoundShape();

    return (PyObject *)self;
}


static void
Shape___dealloc__(Shape *self)
{
    delete self->shape;

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
    btTransform transform = btTransform::getIdentity();
    transform.setOrigin(btVector3(center_x, center_y, center_z));
    transform.setRotation(btQuaternion(
        rotation_x, rotation_y, rotation_z, rotation_w
    ));
    self->shape->addChildShape(transform, capsule);
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
    btTransform transform = btTransform::getIdentity();
    transform.setOrigin(btVector3(center_x, center_y, center_z));
    transform.setRotation(btQuaternion(
        rotation_x, rotation_y, rotation_z, rotation_w
    ));
    self->shape->addChildShape(transform, cone);
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

    self->shape->addChildShape(btTransform::getIdentity(), convex_hull_shape);
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

    auto cylinder = new btCylinderShape(
        btVector3(radius, height * .5, radius)
    );
    btTransform transform = btTransform::getIdentity();
    transform.setOrigin(btVector3(center_x, center_y, center_z));
    transform.setRotation(btQuaternion(
        rotation_x, rotation_y, rotation_z, rotation_w
    ));
    self->shape->addChildShape(transform, cylinder);
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
    self->shape->addChildShape(btTransform::getIdentity(), plane);
    return PyCapsule_New(plane, 0, plane_capsule_destructor);
}


static PyObject *
Shape_add_mesh(Shape *self, PyObject *args)
{
    int num_vertices;
    double *vertices = 0;
    int num_triangle_indices;
    int *triangle_indices = 0;
    if (!PyArg_ParseTuple(
        args, "iLiL",
        &num_vertices, &vertices,
        &num_triangle_indices, &triangle_indices
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
    self->shape->addChildShape(btTransform::getIdentity(), bvh_tri_mesh);

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
    btTransform transform = btTransform::getIdentity();
    transform.setOrigin(btVector3(center_x, center_y, center_z));
    transform.setRotation(btQuaternion(
        rotation_x, rotation_y, rotation_z, rotation_w
    ));
    self->shape->addChildShape(transform, box);
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
    btTransform transform = btTransform::getIdentity();
    transform.setOrigin(btVector3(center_x, center_y, center_z));
    self->shape->addChildShape(transform, sphere);
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
    "gamut.physics._physics",
    0,
    sizeof(struct ModuleState),
    module_methods,
    0,
    0,
    0,
    module_free
};


PyMODINIT_FUNC
PyInit__physics()
{
    ModuleState *state = 0;
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    if (!module){ goto error; }

    if (PyState_AddModule(module, &module_PyModuleDef) == -1){ goto error; }
    state = (ModuleState *)PyModule_GetState(module);

    if (!define_world_type(module)){ goto error; }
    if (!define_body_type(module)){ goto error; }
    if (!define_shape_type(module)){ goto error; }

    state->api = GamutMathApi_Get();
    if (!state->api){ goto error; }

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

