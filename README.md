# collective.translators

Deepl

## Features

TODO: List our awesome features

## Installation

Install collective.translators with `pip`:

```shell
pip install collective.translators
```

And to create the Plone site:

```shell
make create_site
```

## Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## Contribute

- [Issue Tracker](https://github.com/collective/collective.translators/issues)
- [Source Code](https://github.com/collective/collective.translators/)

## License

The project is licensed under GPLv2.

## Credits and Acknowledgements 🙏

Crafted with care by **Generated using [Cookieplone (0.8.1)](https://github.com/plone/cookieplone) and [cookiecutter-plone (f3a6293)](https://github.com/plone/cookiecutter-plone/commit/f3a6293bd1d64bcb7ff67e4ae53fc4ee5223e7c1) on 2024-11-30 11:19:21.252928**. A special thanks to all contributors and supporters!

## Adding a New Tool

If you would like to add a new translation tool, follow these steps:

1. **Create a New Directory for the Translation Tool**

   - Create a new directory for the translation tool inside the `src` folder of your Plone add-on:  
     `[collective.translators/src/collective/translators/{YOUR_TOOL}]`.

   - Inside the new directory, add the following files:
     - `__init__.py`
     - `utility.py`
     - `configure.zcml`

   - The `__init__.py` file should be empty. For the other files, follow the structure of the already implemented tools with the same filenames.

   - Note: The `available_languages` method in the `utility.py` file can return an empty array. In this case, it will be assumed that the tool can translate between any languages.

2. **Update the Add-on Configuration**

   - Register the new tool in your add-on's main `configure.zcml` file:  
     `[collective.translators/src/collective/translators/configure.zcml]`.

   - Add the following line:  
     `<include package=".{YOUR_ADDON}" />`

3. **Create the Registry for Your New Tool**

   - Open the `interfaces.py` file:  
     `[collective.translators/src/collective/translators/interfaces.py]`.

   - Add your new interface, following the structure of the others already implemented there.

   - Open the `main.xml` file:  
     `[collective.translators/src/collective/translators/profiles/default/registry/main.xml]`.

   - Add the configuration for your tool, following the structure of the other entries. It should look like this:

   <records interface="collective.translators.interfaces.IYourToolControlPanel">
       <value key="enabled">False</value>
       <value key="order">30</value>
       <value key="source_languages"></value>
       <value key="target_languages"></value>
       <value key="api_key">YOUR_TOOL_API_KEY</value>
   </records>

4. **Create your personalized control panel** 
Inside the controlpanel folder [collective.translators/src/collective/translators/controlpanel] open "controlpanel.py" and add the configuration of your tool's controlpanel and the adapter. Then, register the adapter and the view in the configure.zcml file within the same folder. Now open the "controlpanel.xml" at [collective.translators/src/collective/translators/profiles/default/controlpanel.xml] and add the configlet.

5. **Test your new tool** 
Access to your new control panel in your Plone site, add your API key and test your tool.
