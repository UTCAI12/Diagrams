# Client

"client side" or "server side" mean that a diagram must be done for client side and/or server side.

## 1. Login and profiles management

-   1.1 User starts the application (client side)
    -   All objects are created
-   1.2 User logs in (client side and server side)
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
-   1.6 User edits his profile (client side and server side)
-   1.7 User disconnects (client side and server side)
    -   Notify server that user is disconnected, then notify other users
-   ~~1.8 User check all online profiles (client side and server side)~~ (consequence of 1.2, all profiles are downloaded at login and after)

## 2. Local music management

-   2.1 User add a music to his local library from a local file (client side)
-   2.2 User add a music to his local library from a distant file (client side and server side)
-   2.3 User edit the music file information (client side and server side)
-   2.4 User edit the visibility of music for the network (client side and server side)

## 3. Listening music

-   3.1 User select a music to start listening (client side and server side)
-   3.2 User pause a music (client side and server side)

## 4. Rating and comments

-   4.1 User add a rating to a music (client side and server side)
-   4.2 User add a comment to a music (client side and server side)

# Server

## All

-   5.1 Server is started (server side)
-   5.2 Server is stopped (server side)
