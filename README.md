Chinook Album Images Database
=============================
Chinook Album Images Database is upgraded version of Chinook Database (c) 2008-2017 Luis Rocha.

Chinook is a popular sample database. You can find Chinook project at [https://github.com/lerocha/chinook-database](https://github.com/lerocha/chinook-database)

In Chinook Album Images Database table Albums is modified by adding Img (BLOB) column. Sql scripts provided will load images into Album.img and "default" Chinook data.
 
Directories
-----------------------------

- **postgress** - chinook-postgress.7z is 7zip compressed version of sql script for loading Chinook image database into Postgress. 
You should have user scott before you execute this script at Postgress db.

- **sqlite** - chinook-sqlite.7z is 7zip compressed version of sql script for creating Chinook database and loading data. Unfortunatelly **THIS SCRIPT DOES NOT WORK**. The problem is that I didn't find decent utiliy that could make an export of sqlite database (in order of foreign key dependencies).
Instead of trying to play chinook-sqlite.7z, please use database file **"chinook.db"**.  I'll be grateful if you can contribute by creating valid sql scripts that could be loaded with SQLite Browser.

- **album_images** - You can find here jpeg images of Albums found by google search & various scripts I've used to download images and "upload" them to Album.Img column.

Contributors
-----------------------------
You are welcome! Be free to create sql scripts for other databases and ask me to merge. 

Thanks! 

License
-----------------------------
**LGPL** 

Copyright (c) Sedad Delalić (Hexo)

Databases in this repository are derivative of Chinook Database (c) 2008-2017 Luis Rocha

Chinook Database
________________
Copyright (c) 2008-2017 Luis Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and 
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
WTFPL 


