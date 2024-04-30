import os

import jinja2

from step_machine.utils.userdata import ASSET_HOME


def render_template(name, target, values):
    """
    Load jinja2 template from ASSET_HOME with the given $name,
    render it with $values and save the output to target, and return the output.
    """
    # Load the template file
    template_loader = jinja2.FileSystemLoader(searchpath=ASSET_HOME)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(name)

    # Render the template with the provided values
    output = template.render(values)

    # Save the output to the specified target file
    with open(target, 'w') as f:
        f.write(output)

    # Return the rendered output
    return output
