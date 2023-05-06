#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    # pytest.main(['-v', '--alluredir', './result'])
    pytest.main(['-v', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
