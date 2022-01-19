# timekeep
Tool for keeping customer time entries. Uses SQLite3 for tracking entries. DB stored locally in user home directory.

## Usage

> This usage section is till under development. Features here may or may not be yet implemented and changes are most likely to happen. Review the *TODO* section below for current status and on-going tasks.

### Create a new record

Syntax:

`timekeep create {so_number} {company_name} {title}`

Example

`timekeep create 123456 "Example Company" "Broken VPN"`

### Add an entry to existing record

Syntax:

`timekeep entry {so_number} {text}`

Text option can be omitted to allow for an "on-the-go" editing. 3 new lines will save the entry in the database and close the application.

### Get entries

Syntax:

`timekeep get entries {so_number}`

Gets all entries for a specified `so_number` number. `so_number` can be omitted to display all entries and their respective SOs 

### Remove entry

Syntax:

`timekeep delete entry {so_number} {entry_number}`

### Remove record

Syntax:

`timekeep delete record {so_number}`

This deletes all also delets all associated records with the SO.

## TODO

### Items to implement
[ ] - Argument parsing.

[ ] - Create new records.

[ ] - Remove new records.

[ ] - Add entries to existent records.

[ ] - Remove entries from existend records.

[ ] - Get all entries associated with the selected record.
