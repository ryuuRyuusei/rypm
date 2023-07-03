# `rypm` - Ryuuzaki Ryuusei Plugin Manager

Manage your Ryuuzaki Ryuusei plugins with ease!

## Installation

Simply run the following command in your terminal:

```bash
pip install git+https://github.com/ryuuRyuusei/rypm.git
```

## Usage

### Add plugin manager cog to your bot

To add the plugin manager cog to your bot instance so you can manage your
plugins from the bot remotely, simply run the following command:

```bash
rypm init
```

### Installing a plugin

To install a plugin, simply run the following command:

```bash
rypm install <git url>
```

Currently, only GitHub repositories are supported, as `rypm` uses raw GitHub
links to download the plugins.

Or, if you want to install a plugin from the bot, you can run the following
command:

```bash
/plugin install url:<git url>
```

### Uninstalling a plugin

To uninstall a plugin, simply run the following command:

```bash
rypm uninstall <plugin name>
```

Or, if you want to uninstall a plugin from the bot, you can run the following

```bash
/plugin uninstall name:<plugin name>
```

### Updating plugins

To update all plugins, simply run the following command:

```bash
rypm update
```

Or, if you want to update all plugins from the bot, you can run the following

```bash
/plugin update
```
