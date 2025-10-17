Scenario (short)

A simple blogging/social-post system:

- Users sign up and have a single Profile (one-to-one).

- Users write Posts (one-to-many: a user → many posts).

- Posts can have many Tags, and Tags apply to many Posts (many-to-many via an association table).

- We’ll include an association table post_tags that has extra metadata.

- We'll include a comments table (optional/advanced) to illustrate extra relationships if you want — I list it below as an extension.

We will use PostgreSQL as the target DB.