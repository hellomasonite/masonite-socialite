from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """Run the migrations."""
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name')
            table.string('email').unique()
            table.string('password').nullable()
            table.string('provider', 100).nullable()
            table.string("access_token", 1000).nullable()
            table.string('remember_token').nullable()
            table.timestamp('verified_at').nullable()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop('users')
