# hubmap-fairness-project
A Python package to measure FAIR principles for HuBMAP datasets.

## Installation

```bash
pip install fair-hubmap
```

## Usage
Run the CLI to assess a HuBMAP dataset

```bash
fair-hubmap assess --dataset-id <HuBMAP_dataset_ID>
```

### Programmatic usage
```
from fair_hubmap import Assessor

assessor = Assessor(dataset_id="HBM123.ABCD.456")
report = assessor.evaluate()
print(report)
```

## Features
* Evaluates Findability, Accessibility, Interoperability, and Reusability.
* Integrates with HuBMAP Data Portal API.
* Generates reports and visualizations.

## TODO
* Use HuBMAP SDK to get public metadata information.
* Create a function that returns the value for a metric (0-1).
* Accomodate results in heat map.
