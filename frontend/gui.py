import tkinter as tk
from backend.get_products import get_products
from backend.functions import stringified_product_requirements, stringified_factories_from_demand
from tkinter import ttk
from dataclasses import dataclass


@dataclass
class Widgets:
    main_frame: tk.Frame

    frame_top: tk.Frame
    frame_left: tk.Frame
    frame_right: tk.Frame

    frame_product: tk.Frame
    label_product: tk.Label
    product_combobox: ttk.Combobox

    frame_simplified: tk.Frame
    simplified_checkbutton: tk.Checkbutton

    frame_demand: tk.Frame
    label_demand: tk.Label
    demand_entry: tk.Entry

    frame_per: tk.Frame
    label_per: tk.Label
    per_entry: tk.Entry

    frame_output: tk.Frame
    output_label: tk.Label

    frame_bottom_buttons: tk.Frame
    button_calculate_requirements: tk.Button
    button_calculate_factories: tk.Button


class Window:
    root: tk.Tk
    products: dict
    products_var: tk.StringVar
    widgets: Widgets
    simplified_production_chains: tk.BooleanVar  # TODO implement
    demand: tk.IntVar
    per: tk.IntVar
    output_text = tk.StringVar
    pad = 5
    geometry = '400x400'
    title = 'Calculator'

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(self.title)
        # self.root.geometry(self.geometry)
        self.products = get_products()
        self.products_var = tk.StringVar(value='Select a product')
        self.simplified_production_chains = tk.BooleanVar(value=True)
        self.demand = tk.IntVar(value=0)
        self.per = tk.IntVar(value=15)
        self.output_text = tk.StringVar(value='There will be displayed results of the calculations')

        self.initialize_ui()

    @property
    def list_of_products(self) -> list:
        return list(self.products.keys())

    def refresh_products(self):
        self.products = get_products()

    def show_warning_simplified(self):
        # TODO implement
        raise NotImplementedError

    def calculate_requirements(self):
        # TODO implement
        raise NotImplementedError

    def calculate_factories(self):
        # TODO implement
        raise NotImplementedError

    def initialize_ui(self):
        # main window frame
        frame_main = tk.Frame(self.root)
        frame_main.pack(side='top', fill='both')

        # frame for inputs
        frame_top = tk.Frame(master=frame_main)
        frame_top.pack(side='top', fill='x')

        # frame for leftmost widgets
        frame_left = tk.Frame(master=frame_top)
        frame_left.pack(side='left', fill='y')

        # frame for rightmost widgets
        frame_right = tk.Frame(master=frame_top)
        frame_right.pack(side='right', fill='y')

        # product selection
        frame_product = tk.Frame(master=frame_left)
        frame_product.pack(side='top', fill='x')

        label_product = tk.Label(master=frame_product, text='Select a product')
        label_product.pack(side='left', padx=self.pad, pady=self.pad)

        combobox = ttk.Combobox(
            master=frame_product,
            textvariable=self.products_var,
            values=self.list_of_products,
            width=20, )
        combobox.pack(side='left', padx=self.pad, pady=self.pad)

        # simplified production chains checkbox
        frame_simplified = tk.Frame(master=frame_left)
        frame_simplified.pack(side='top', fill='x')

        simplified_checkbutton = tk.Checkbutton(
            master=frame_simplified,
            variable=self.simplified_production_chains,
            text='Simplified production chains'
        )
        simplified_checkbutton.pack(side='left', padx=self.pad, pady=self.pad)

        # demand entry and Co.
        frame_demand = tk.Frame(master=frame_right)
        frame_demand.pack(side='top', fill='x')

        label_demand = tk.Label(master=frame_demand, text='Enter demand')
        label_demand.pack(side='left', padx=self.pad, pady=self.pad)

        demand_entry = tk.Entry(master=frame_demand, textvariable=self.demand)
        demand_entry.pack(side='right', padx=self.pad, pady=self.pad)

        # demand entry and Co.
        frame_per = tk.Frame(master=frame_right)
        frame_per.pack(side='top', fill='x')

        label_per = tk.Label(master=frame_per, text='Enter period in days')
        label_per.pack(side='left', padx=self.pad, pady=self.pad)

        per_entry = tk.Entry(master=frame_per, textvariable=self.per)
        per_entry.pack(side='right', padx=self.pad, pady=self.pad)

        # output box
        frame_output = tk.Frame(master=frame_main)
        frame_output.pack(side='top', padx=self.pad, pady=self.pad)

        output_label = tk.Label(master=frame_output, textvariable=self.output_text, height=5, width=40)
        output_label.pack(side='top', padx=self.pad, pady=self.pad, fill='both')

        # frame for buttons at the bottom of the window
        frame_bottom = tk.Frame(master=frame_main)
        frame_bottom.pack(side='top', padx=self.pad, pady=self.pad)

        button_calculate_requirements = tk.Button(
            master=frame_bottom,
            command=self.calculate_requirements,
            text='Calculate requirements'
        )
        button_calculate_requirements.pack(side='left')

        button_calculate_factories = tk.Button(
            master=frame_bottom,
            command=self.calculate_factories,
            text='Calculate factories'
        )
        button_calculate_factories.pack(side='left')

        self.widgets = Widgets(
            main_frame=frame_main,
            frame_left=frame_left,
            frame_right=frame_right,
            frame_top=frame_top,
            product_combobox=combobox,
            label_product=label_product,
            frame_product=frame_product,
            frame_simplified=frame_simplified,
            simplified_checkbutton=simplified_checkbutton,
            frame_demand=frame_demand,
            label_demand=label_demand,
            demand_entry=demand_entry,
            frame_per=frame_per,
            label_per=label_per,
            per_entry=per_entry,
            frame_output=frame_output,
            output_label=output_label,
            frame_bottom_buttons=frame_bottom,
            button_calculate_requirements=button_calculate_requirements,
            button_calculate_factories=button_calculate_factories,
        )


if __name__ == "__main__":
    w = Window()
    w.root.mainloop()
