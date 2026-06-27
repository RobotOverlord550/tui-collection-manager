from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer, Input
from textual.screen import Screen
import save_data


# initialize with column names
rows = [("Name", "Description", "Quantity")]
data = []


class AddItemScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Name")
        yield Input(placeholder="Description")
        yield Input(placeholder="Quantity")


class CollectionManager(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("a", "add_item", "Add Item"),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*rows[0])
        table.add_rows(rows[1:])

    def action_add_item(self) -> None:
        self.push_screen(AddItemScreen())


def initialize_rows():
    # load user data
    data = save_data.load_data()

    # loop through data and build data-table
    for d in data:
        name = d["name"]
        desc = d["description"]
        quantity = d["quantity"]

        row = (name, desc, quantity)
        rows.append(row)

    return data


if __name__ == "__main__":
    data = initialize_rows()
    app = CollectionManager()
    app.run()
