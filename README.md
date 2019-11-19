# langclass

**langclass** is a model for predicting a programming language from its source
code.

---

## Live version

A live version is deployed here: <http://langclass.kevinlui.org/>

---

## Model details

See <https://kevinlui.org/posts/langclass/>

---

## Usage

Everything should be accessible via `make` commands. The main ones are

- `make data`: Retrieves external data and save relevant parts as a `csv` file.
- `make train`: Trains the model.
- `make web-develop`: Starts a webserver running on port 5000.
- `make web-deploy`: Starts a webserver running on port 80.
