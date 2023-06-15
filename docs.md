# MongoDB

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
```json
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

## FAQ / Issues
**Q:** Why ctx.response.send_message("message") instead of ctx.send("Message")? 

**A:** Out of nowhere, commands started passing Interaction objects to ctx instead of Context objects. So we're stuck using that :(