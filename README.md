# ROS1 TO ROS2 Autotest

# Test environment
Linux: ububtu

ROS: ros1

Autoware: Autoware4

python: python3.6


# Test Frame
python+pytest+allure

![frame](/docs/images/frame.png)

![test flow](/docs/images/test_flow.png)

## Deployment

[Installation instructions](docs/install.md)

## How to run cases?

```buildoutcfg
python3 run.py -h  # help

python3 run.py -f perception  # run perception cases

python3 run.py -f perception -r # run perception cases with rviz

python3 run.py -f planning  # run perception cases

python3 run.py -f planning -r  # run perception cases with rviz

python3 run.py -f planning,perception    # run planning and perception cases
```

## How to add cases?

1. [Add perception cases](docs/add_perception_cases.md)

2. [Add planning cases](docs/add_planning_cases.md)


## About Pytest and Allure

Pytest official website: https://docs.pytest.org/en/stable/

Allure official website: https://docs.qameta.io/allure/#_pytest


## Development usage
if docker updated, need to exec:
 - docker pull registry.autocore.ai/autotest/devel
 - docker pull registry.autocore.ai/autotest/debug
 - docker pull registry.autocore.ai/autotest/data
 
 
 