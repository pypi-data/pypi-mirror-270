# kabaret.flow_entities

A `kabaret.flow` extension providing searchable large collections of entities, stored in a mongodb.

Create your Entities
====================

Entities are a queryable collection of objects. 

In order to define an entity, you must inherit
the `Entity` class and add some `Property` in it:

```python
from kabaret.flow_entities.entities import Entity, Property

class Asset(Entity):

    asset_type = Property()
    asset_family = Property()
    
    status = Property()

```

You can also add classic relations like `Param` and `Child` and build a whole branch
inside your entity. But keep in mind that the `Propery` relations will be the only ones
usable in your queries.

Once you have an Entity defined, you must use it in an `EntityCollection`:

```python
from kabaret.flow_entities.entities import EntityCollection, CreateEntitiesAction, DeleteEntitiesAction

class Assets(EntityCollection):

    # Those actions are provided for convenience,
    # you will probably want to define your owns:
    create_assets = flow.Child(CreateEntitiesAction)
    delete_assets = flow.Child(DeleteEntitiesAction)

    @classmethod
    def mapped_type(cls):
        # This tells which entity is show in 
        # this collection:
        return Asset
```

When using the `Assets` collection in your flow, the users will see a
table with "Asset Type", "Asset Family" and "Status" columns.

This table is more efficient than a `kabaret.flow.Map` and can retrieve thousands of items
in a fraction of seconds.

Still, the `EntityCollection` class inherits `kabaret.flow.DynamicMap` so you can use all the classic
customization points (`columns()`, `_fill_row_style()`, etc...).


Filter your Entities
====================

The `EntityCollection.query_filter()` method can be overidden to return a mongodb filter and
restrict the list of displayed entities. You can for example decide to show only the Assets
with a "WIP" status:

```python
class Assets(EntityCollection):

    create_assets = flow.Child(CreateEntitiesAction)
    delete_assets = flow.Child(DeleteEntitiesAction)

    @classmethod
    def mapped_type(cls):
        return Asset

    def query_filter(self):
        """
        Listing only assets with a WIP status
        """ 
        return {"status": "WIP"}
```

Now you can add some `Action` and `Param` on your collection to control 
the returned value of `query_filter()`.

Note that only the `Property` relations of your entity can be used 
in the filter !

The query filter must be a valid argument for a mongodb `collection.find()` call. Here is some documentation about it: https://docs.mongodb.com/manual/tutorial/query-documents/


Multiple Entity Views
=====================

The `EntityCollection.collection_name()` method can be overidden to point
to another entity collection. This is usefull if you want to display some
entities with a different query filter in different place of your flow.

Here is an example of showing only unfinished tasks assigned to the
current user from a collection of tasks managed in an `admin` section of the
project:

```python

class MyTodo(EntityCollection):

    @classmethod
    def mapped_type(cls):
        # be sure to match the source
        # collection here:
        return AwesomeTask

    def collection_name(self):
        return self.root().project().admin.all_tasks.collection_name()
    
    def query_filter(self):
        return {
            "assignee": getpass.getuser(), 
            "status": {"$in": ["NYS", "WIP"]},
        }
```

MongoDB Connection
==================

The entities are stored as documents in collections of a `mongodb`.

In order for your `EntityCollection` to connect to the database, you
must add an `EntityStore` somewhere in your project and implement a `get_entity_store()` method on your project's root.

A classic aproach is to use an `admin` group in your project:
```python

from kabaret.flow_entities.store import EntityStore

class Admin(flow.Object):

    entity_store = flow.Child(EntityStore)
    
class AwesomePipeline(flow.Object):

    admin = flow.Child(Admin)

    def get_entity_store(self):
        return self.admin.entity_store


```

The `EntityStore` has an `uri` param that you will need to 
set before showing or creating entity. The default value connects to a local mongodb database using the default port and options. Contact your beloved IT support team and ask them the value to use for production.

Here is a detailed documentation of the URI syntaxe: https://docs.mongodb.com/manual/reference/connection-string/

Demo
====

See `kabaret.flow_entities.demo` for more demo code.

Create a project with the type `kabaret.flow_entities.demo.EntitiesDemo` to see it in action.

