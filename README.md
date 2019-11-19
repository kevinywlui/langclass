# langclass

**langclass** is a model for predicting a programming language from its source
code.

---

## Live version

A live version is deployed here: <http://langclass.kevinlui.org/>

---

## High level details

### Data source

The data was retrieve from the [Rosetta Code
Project](https://rosettacode.org/wiki/Rosetta_Code) using this git repo:
<https://github.com/acmeism/RosettaCodeData>. The features is a code snippet
and the labels are programming languages. For example.

### Tokenization

We consider 2 different tokenizers.

- character-level tokenization. `print('Hello World') -> ['p', 'r', 'i', 'n' 't', '(', ...]`

- split on non-alphanumerical. `print('Hello World') -> ['print', '(', 'Hello',
  'World', ')']`

### Vectorization

After tokenizing, we consider consider 1-grams followed by feature hashing
modulo 4098. We also do the same with 2-grams.

### Classifier

We use [lightgbm](https://lightgbm.readthedocs.io/en/latest/) with default
parameters. There's a lot of tuning to be done but that wasn't my main interest
so I'm putting it off.

### Feature Importance

A fun thing I did was feature importance extraction despite feature hashing.
See the live-version for an explanation for how I did this.

The top features for character-level 2-grams are:

`[';\n', ')\n', ' (', ', ', ' =', '= ', 't(', 't ', 'in', '# ']`

The top features for 1-grams where we split on non-alphanumericals are:

`[';', '=', '.', ':', 'print', ',', '"', '#', ')', '-']`


---

## Usage

Everything should be accessible via `make` commands. The main ones are

- `make data`: Retrieves external data and save relevant parts as a `csv` file.
- `make train`: Trains the model.
- `make web-develop`: Starts a webserver running on port 5000.
- `make web-deploy`: Starts a webserver running on port 80.
