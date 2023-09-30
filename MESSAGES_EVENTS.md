# Messages events

## Message types through the socket

### Users

-   USER_CONNECT (User) : Message send by the user who wants to connect to the server
-   USER_CONNECTED (List\<User>) : Message send by the server to the new connected user (in response to USER_CONNECT)
-   USER_DISCONNECT (User) : Message send by the user who wants to disconnect from the server
-   USER_UPDATE (User) : Message send by the user who wants to update his profile
-   GET_USER (UUID) : Message send by the user who wants to get the full data model of a user

### Tracks

-   GET_TRACK (UUID) : Message send by the user who wants to get the full data model of a track
-   DOWNLOAD_TRACK (Track) : Message send by the server to the user who wants to download a track
-   PUBLISH_TRACK (Track) : Message send by the user who wants to publish a track
-   UNPUBLISH_TRACK (Track) : Message send by the user who wants to unpublish a track
-   UPDATE_TRACK (Track) : Message send by the user who wants to update a track

### Comments and ratings

-   PUBLISH_COMMENT (Comment) : Message send by the user who wants to publish a comment
-   PUBLISH_RATING (Rating) : Message send by the user who wants to publish a rating

## Event types emitted by the model

### Users

-   NEW_USER(User) : Emitted when a new user is added
-   NEW_USERS() : Emitted when new users are added
-   UPDATE_USER(User) : Emitted when a user is updated
-   DELETE_USER(User) : Emitted when a user is deleted

### Tracks

-   NEW_TRACK (Track) : Emitted when a new track is added (or published by an other user)
-   NEW_TRACKS () : Emitted when new tracks are added (or published by an other user)
-   UPDATE_TRACK (Track) : Emitted when a track is updated (or updated by an other user)
-   DELETE_TRACK (Track) : Emitted when a track is deleted (or unpublished by an other user)
-   DOWNLOADED_TRACK (Track) : Emitted when a track is downloaded

### Comments and ratings

-   NEW_COMMENT (Comment) : Emitted when a new comment is added (or published by an other user)
-   NEW_RATING (Rating) : Emitted when a new rating is added (or published by an other user)
