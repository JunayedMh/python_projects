## Build a contact book that stores and manages contacts.

Rules:
- Each contact: {'name': ..., 'phone': ..., 'email': ...}

**Menu:**

1. Add contact
2. View all contacts
3. Search by name
4. Delete by name
5. Update phone or email
6. Exit
  - Phone validation: exactly `11` digits, all `numbers`.
  - Email validation: must contain `'@'` and `'.'`
  - No `duplicate` names allowed.
  - Search and delete are case-insensitive.
  - Show total contact `coun`t when viewing all.