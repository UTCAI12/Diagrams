# Sequence diagrams

-   "client side" is the client that performs the action,
-   "server side" is the server linked to the client that performs the action,
-   "owner side" is the client that owns the data that is the subject of the action,
-   "others side" is the other clients that are connected to the server and that are not the client that performs the action.

# Summary

| Number  | Name                                                      | Client side | Server side | Owner side | Others side |
| ------- | --------------------------------------------------------- | ----------- | ----------- | ---------- | ----------- |
| 1.1     | User starts the application                               | OK          | /           | /          | /           |
| 1.2     | User logs in                                              | OK          | TODO        | /          | TODO        |
| ~~1.3~~ | ~~User import his profile from a file~~                   |             |             |            |             |
| 1.4     | User export his profile to a file                         | OK          | /           | /          | /           |
| ~~1.5~~ | ~~User creates a new profile~~                            |             |             |            |             |
| 1.6     | User edits his profile                                    | OK          | OK          | /          | OK          |
| 1.7     | User disconnects                                          | TODO        | TODO        | /          | TODO        |
| ~~1.8~~ | ~~User check all online profiles~~                        |             |             |            |             |
|         |                                                           |             |             |            |             |
| 2.1     | User add a music to his local library from a local file   | OK          | /           | /          | /           |
| 2.2     | User add a music to his local library from a distant file | OK          | OK          | OK         | /           |
| 2.3     | User edit the music file information                      | OK          | OK          | /          | OK          |
| ~~2.4~~ | ~~User edit the visibility of music for the network~~     |             |             |            |             |
|         |                                                           |             |             |            |             |
| 3.1     | User select a music to start listening                    | OK          | TODO        | TODO       | /           |
| 3.2     | User pause a music                                        | OK          | /           | /          | /           |
|         |                                                           |             |             |            |             |
| 4.1     | User add a rating to a music                              | OK          | OK          | /          | OK          |
| 4.2     | User add a comment to a music                             | OK          | OK          | /          | OK          |
|         |                                                           |             |             |            |             |
| 5.1     | Server is started                                         | /           | OK          | /          | /           |
| 5.2     | Server is stopped                                         | /           | OK          | /          | OK          |

# Details

## 1. Login and profiles management

-   1.1 User starts the application (client side)
    -   All objects are created
-   1.2 User logs in (client, server and others side)
    -   User set his login and password
    -   If correct, client send message to server to notify the new connection
-   ~~1.3 User import his profile from a file (client side)~~
    -   ~~User select a file, profile imported~~
    -   ~~THIS IS NOT A LOGIN, after, user must login~~ (consequence of 1.2)
-   1.4 User export his profile to a file (client side)
    -   User select a file, profile exported
-   ~~1.5 User creates a new profile (client side)~~
    -   ~~User set all profile information~~
    -   ~~THIS IS NOT A LOGIN, after, user must login~~ (consequence of 1.2)
-   1.6 User edits his profile (client, server and others side)
-   1.7 User disconnects (client, server and others side)
    -   Notify server that user is disconnected, then notify other users
-   ~~1.8 User check all online profiles (client side and server side)~~ (consequence of 1.2, all profiles are downloaded at login and after)

## 2. Local music management

-   2.1 User add a music to his local library from a local file (client side)
-   2.2 User add a music to his local library from a distant file (client, server and owner side)
-   2.3 User edit the music file information (client, server and others side)
-   ~~2.4 User edit the visibility of music for the network (client side and server side)~~ (consequence of 2.3)

## 3. Listening music

-   3.1 User select a music to start listening (client, server and owner side)
-   3.2 User pause a music (client side and server side)

## 4. Rating and comments

-   4.1 User add a rating to a music (client, server and others side)
-   4.2 User add a comment to a music (client, server and others side)

# Server

## All

-   5.1 Server is started (server side)
-   5.2 Server is stopped (server and others side)
