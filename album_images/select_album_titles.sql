/* I've used result of this query as search for google image search */
select "Artist"."Name" || ' ' || "Title" from "Album", "Artist" where "Artist"."ArtistId" = "Album"."ArtistId"