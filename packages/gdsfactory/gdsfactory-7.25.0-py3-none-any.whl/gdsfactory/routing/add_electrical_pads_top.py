from __future__ import annotations

from functools import partial

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.components.pad import pad_array as pad_array_function
from gdsfactory.components.wire import wire_straight
from gdsfactory.port import select_ports_electrical
from gdsfactory.routing.route_quad import route_quad
from gdsfactory.typings import (
    Callable,
    ComponentSpec,
    Float2,
    LayerSpec,
    Strs,
)

_wire_long = partial(wire_straight, length=200.0)


@gf.cell_with_child
def add_electrical_pads_top(
    component: ComponentSpec = _wire_long,
    direction: str = "top",
    spacing: Float2 = (0.0, 100.0),
    pad_array: ComponentSpec = pad_array_function,
    select_ports: Callable = select_ports_electrical,
    port_names: Strs | None = None,
    layer: LayerSpec = "MTOP",
    **kwargs,
) -> Component:
    """Returns new component with electrical ports connected to top pad array.

    Args:
        component: to route.
        direction: sets direction of the array (top or right).
        spacing: component to pad spacing.
        pad_array: function for pad_array.
        select_ports: function to select electrical ports.
        port_names: optional port names. Overrides select_ports.
        layer: for the routes.

    Keyword Args:
        ports: Dict[str, Port] a port dict {port name: port}.
        prefix: select ports with port name prefix.
        suffix: select ports with port name suffix.
        orientation: select ports with orientation in degrees.
        width: select ports with port width.
        layers_excluded: List of layers to exclude.
        port_type: select ports with port type (optical, electrical, vertical_te).
        clockwise: if True, sort ports clockwise, False: counter-clockwise.


    .. plot::
        :include-source:

        import gdsfactory as gf

        c = gf.components.wire_straight(length=200.)
        cc = gf.routing.add_electrical_pads_top(component=c, spacing=(-150, 30))
        cc.plot()

    """
    c = Component()
    component = gf.get_component(component)
    ref = c << component

    ports_electrical = (
        [ref[port_name] for port_name in port_names]
        if port_names
        else list(select_ports(ref.ports, **kwargs).values())
    )

    if direction == "top":
        pads = c << gf.get_component(
            pad_array, columns=len(ports_electrical), rows=1, orientation=270
        )
    elif direction == "right":
        pads = c << gf.get_component(
            pad_array, columns=1, rows=len(ports_electrical), orientation=270
        )
    pads.x = ref.x + spacing[0]
    pads.ymin = ref.ymax + spacing[1]
    ports_pads = list(pads.ports.values())

    ports_pads = gf.routing.sort_ports.sort_ports_x(ports_pads)
    ports_component = gf.routing.sort_ports.sort_ports_x(ports_electrical)

    for p1, p2 in zip(ports_component, ports_pads):
        _ = c << route_quad(p1, p2, layer=layer)

    c.add_ports(ref.ports)

    # remove electrical ports
    for port in ports_electrical:
        c.ports.pop(port.name)

    c.add_ports(pads.ports)
    c.copy_child_info(component)
    c.auto_rename_ports(prefix_electrical=f"elec-{component.name}-")
    return c


if __name__ == "__main__":
    import gdsfactory as gf

    # c = gf.components.straight_heater_metal()
    # c = gf.components.mzi_phase_shifter_top_heater_metal()
    # cc = gf.routing.add_electrical_pads_top(component=c, spacing=(-150, 30))
    c = add_electrical_pads_top()
    c.show(show_ports=True)
