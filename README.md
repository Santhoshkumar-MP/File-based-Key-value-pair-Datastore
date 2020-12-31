# File-based-Key-value-pair-Datastore
CRD operation performed in Dictionary based Datastore

File based key value datastore that supports the basic CRD(create, read and delete) operations.This Data store is meant to be in used as a local storage for one single process on one laptop.The data store must be exposed as a library to client that can instantiate a class and work with data store.
The data store will support the following functional requirements.
.>It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable loaciton on the laptop.
.>A new key-value pair can be added to the data store using Create operation.The key is always a string-cappped at 32chars.the value is always a JSON object-capped at 16KB.
.>If create is invoked for an existing key, an appropriate erroe must be returned.
.>A Read operation on akey can be performed my promed by providing the key,and receiving the value in response, as a JSON object.
.>A Delete operation can be performed by providing the key.
.>Every key supports setting a TIME TO LIVE property when it is created.This property is optional.If provided,it will be evaluated as an integer defining the number of seconds the key must be retained in the data store.Once the TIME TO LIVE for a key has expired, the key will no longer be availiable for Read or Delete operation.
.>Appropriate error responses must always be returned to a client if it uses the data store in unexpected way or breaches any limits.
