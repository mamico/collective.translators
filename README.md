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
