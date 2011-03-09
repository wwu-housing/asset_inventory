Made by Jon Geller 3/9/2011
ResTek of Western Washington University
Using Python/Django as the:
Housing Inventory Management System
-----------------------------------------

This project contain several features:

On the main page there are links to each of the objects handeled by the database as well as links to the inventory printout page and aged inventory list. The printout and aged list are both provided as special use case pages discussed during analysis of the inventory needs.

On each page accessed through the menu you will find a list of all items stored in that object table. From here, you can view each item's information in detail layout. Also from here you can edit each items as needed.

Some of things to point out: 

First, the models defined in the models.py file are modified by the forms.py file if you use the web site created to add and edit data.

Second (a bit confusing), the Esign forms behave in a special fashion. Each esign form can have many devices associated with them, and devices can have more than one esign, you can add devices to the esign pages, but not esigns to the device pages.

Third, the table structure which is the pdf file in the repository, show how each of the tables relies on the device model, which you can see in the model.py file, but its still important to point out. This PDF is currently NOT the final form found in the model.py file, but rather a design spec file.


-Jon