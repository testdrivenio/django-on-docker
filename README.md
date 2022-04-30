# Dockerizing Django with Postgres, Gunicorn, and Nginx

## Want to learn how to build this?

Check out the [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).

## Want to use this project?

### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

### Pre Commit Hooks

To enable pre-commit hooks:
1. Install [pre-commit](https://pre-commit.com/) using `pip3 install pre-commit`.
2. Set up git hooks script using `pre-commit install`.

This will run following pre-commit hooks on diff of HEAD git SHA.

- **[Deprecations]** A quick check for the deprecated `.warn()` method of python loggers
- **[Deprecations]** A quick check on python3.6+ type annotations are present instead of type comments
- **[Static Linter]** Using flake8 and some other checks.
- **[Linter]** Running pylint
- **[Code Formatter]**  Run Black: The uncompromising Python code formatter
- **[Static Analysis]** A quick static analyzer like pydocstyle static analysis tool for checking compliance with Python docstring conventions.
- **[Static Analysis]** A quick check to find unused Python code. 
- **[Security]** A quick check on Python requirements for known security vulnerabilities
- **[Security]** Run Bandit, the tool for finding common security issues in Python code
- **[Security][Python Project Dependencies]** Enabling something like, skjold to check for  Security audit Python project dependencies against security advisory databases
- **[Code Organizer]** Run a Python import rewriter for ex: zimports
- **[Production Server Cleaning]** A quick check for debugger statements and py37+ `breakpoint()` calls in python source.
