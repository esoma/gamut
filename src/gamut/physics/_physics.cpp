
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// bullet
#define BT_USE_DOUBLE_PRECISION
#include "btBulletDynamicsCommon.h"
#include <iostream>

#define ASSERT(x) if (!x){ std::cout << __FILE__ << ":" << __LINE__ << std::endl; exit(1); }


struct World
{
    PyObject_HEAD
    btDefaultCollisionConfiguration *collision_config;
    btCollisionDispatcher *collision_dispatcher;
    btDbvtBroadphase *broadphase;
    btSequentialImpulseConstraintSolver *solver;
    btDiscreteDynamicsWorld *world;
};


struct Body
{
    PyObject_HEAD
    btCollisionShape *collision_shape;
    btDefaultMotionState *motion_state;
    btRigidBody *body;
};


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
World_add_body(World *self, Body *body)
{
    self->world->addRigidBody(body->body);
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
    double time = PyFloat_AsDouble(args);
    if (PyErr_Occurred()){ return 0; }
    self->world->stepSimulation(time);
    Py_RETURN_NONE;
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
    btVector3 gravity = self->world->getGravity();
    return Py_BuildValue("fff", gravity.x(), gravity.y(), gravity.z());
}


int
World_Setter_gravity(World *self, PyObject *value, void *)
{
    double x, y, z;
    if (!PyArg_ParseTuple(value, "ddd", &x, &y, &z)){ return -1; }
    self->world->setGravity(btVector3(x, y, z));
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
    static char *kwlist[] = {NULL};
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "", kwlist
    )){ return 0; }

    Body *self = (Body*)cls->tp_alloc(cls, 0);

    self->collision_shape = new btBoxShape(btVector3(1, 1, 1));
    self->motion_state = new btDefaultMotionState(btTransform::getIdentity());
    btRigidBody::btRigidBodyConstructionInfo info(
        1,
        self->motion_state,
        self->collision_shape
    );
    self->body = new btRigidBody(info);

    return (PyObject *)self;
}


static void
Body___dealloc__(Body *self)
{
    delete self->body;
    delete self->motion_state;
    delete self->collision_shape;

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef Body_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyMethodDef Body_PyMethodDef[] = {
    {0, 0, 0, 0}
};


static PyGetSetDef Body_PyGetSetDef[] = {
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


// module
// ----------------------------------------------------------------------------

static PyMethodDef module_methods[] = {
    {0, 0, 0, 0}
};


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut.physics._physics",
    0,
    0,
    module_methods,
    0,
    0,
    0
};


PyMODINIT_FUNC
PyInit__physics()
{
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    if (!module){ goto error; }

    if (!define_world_type(module)){ goto error; }
    if (!define_body_type(module)){ goto error; }

    return module;
error:
    Py_CLEAR(module);
    return 0;
}
