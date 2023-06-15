# MongoDB

## Index
[Getting Started](#Getting-Started)
<br>
[Key Concepts](#Key-Concepts)
<br>
[Database Functions](#Database-Functions)
<br>
[FAQ / Issues](#FAQ-/-Issues)


## Getting Started
[Setup](https://www.mongodb.com/docs/atlas/getting-started/)

[PyMongo Tutorial](https://www.mongodb.com/languages/python/pymongo-tutorial)

[PyMongo Docs](https://pymongo.readthedocs.io/en/stable/tutorial.html)

[Interaction Object Docs](https://discordpy.readthedocs.io/en/stable/interactions/api.html)
<br>
<small>[Interaction Responses](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction.response)</small>

## Key Concepts
**Atlas** = The name of the service which is part of MongoDB

**Clusters** = A collection of datasets distributed across many shards (servers). Basically the server(s) which can hold multiple databases

**Collections** = The database. Holds documents

**Documents** = The data. Each document contains data in the format of BSON (binary JSON)

*Ex.*
```bson
//example of a  single document
{
    _id: ObjectId("2345923849234239"),
    name: { 
        first: "Alan", 
        last: "Turing" 
    },
    birth: new Date('Jun 23, 1912'),
    death: new Date('Jun 07, 1954'),
    contribs: [ "Turing machine", "Turing test", "Turingery" ],
    views : NumberLong(1250000)
}
```

**Users** = Users that have permission within the database. Each has a username and password

## Database Functions
```py
#Find document in collection
collection.find_one({"key": "value"}) #finds document by search query


#Update data in document
collection.update_one(query, update)
query = {"key": "value"}
update = { #where $set is an operator that can be changed
    '$set': {
        'key': 'value
    }
}
"""
$set: Sets the value of a field.
$unset: Removes a field from a document.
$inc: Increments the value of a numeric field by a specified amount.
$mul: Multiplies the value of a numeric field by a specified amount.
$rename: Renames a field.
$push: Adds an element to an array field.
$pop: Removes the first or last element from an array field.
$pull: Removes elements from an array field that match a specified condition.
$addToSet: Adds an element to an array field only if it doesnt already exist.
$each: Modifies the behavior of array operators to apply the operation to each element individually.
$slice: Limits the number of elements in an array field.
$sort: Sorts the elements in an array field.
$elemMatch: Matches documents that contain an array field with at least one element matching the specified condition.
"""
```

## FAQ / Issues
**Q:** Why ctx.response.send_message("message") instead of ctx.send("Message")? 

**A:** Out of nowhere, commands started passing Interaction objects to ctx instead of Context objects. So we're stuck using that :(