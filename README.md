# ROS1 TO ROS2 Autotest

# Test environmental
Linux: ububtu

Autoware: Autoware4

python: python3.6


# Test Frame
python+pytest+allure

## Deployment
[Installation instructions](docs/install.md)

## How to run cases?

```buildoutcfg
python3 run.py -h  # help

python3 run.py -f perception  # run perception cases

python3 run.py -f planning  # run perception cases

python3 run.py -f planning,perception    # run planning and perception cases
```

## How to add cases?

[Add perception cases](docs/add_perception_cases.md)

[Add planning cases](docs/add_planning_cases.md)

