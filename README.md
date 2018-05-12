# Improvement Authority Wordpress

This is a Wordpress implementation of the Improvement Authority project.

It is built using Wordpress and Bedrock, which is inspired by the [Twelve-Factor App](http://12factor.net/) methodology
 including the [WordPress specific version](https://roots.io/twelve-factor-wordpress/).

## Features

* Better folder structure
* Dependency management with [Composer](http://getcomposer.org)
* Easy WordPress configuration with environment specific files
* Environment variables with [Dotenv](https://github.com/vlucas/phpdotenv)
* Autoloader for mu-plugins (use regular plugins as mu-plugins)
* Enhanced security (separated web root and secure passwords with [wp-password-bcrypt](https://github.com/roots/wp-password-bcrypt))

## Requirements

* PHP >= 5.6
* Composer - [Install](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx)

## Installation Guide

This guide assumes you have `php` available on your path and are running commands from within the `code` directory.  Local development will rely on the internal PHP development server.

1.  Install dependencies by running `composer install`.

2.  Update your `.env.example` file to match your environment's desired settings (Database, hostname, etc).  Make sure your database exists and the user has the correct rights.

3.  Run the local server with `php -S localhost:8080 -t web`

4.  Head to http://localhost:8080 in your browser and configure your WP install.

## Local Development

If you're build is up and running and you'd like to make improvements to the frontend or template you should head into
`web/app/themes/wordchallenge` directory and run `gulp`.  This assumes your webserver is running at port `8080`.

## Database Snapshots

If you're wanting to get up and running with an existing database snapshot check in the `/db` directory for data snapshots.

## Authbind on OS X

If you use the Makefile in the project root, you'll need authbind.  See [here](https://medium.com/@steve.mu.dev/setup-authbind-on-mac-os-6aee72cb828) for a guide on authbind for OS X.
