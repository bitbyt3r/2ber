#!/bin/bash

set -e

cd backend
coverage run --source=tuber -m pytest
bash <(curl -s https://codecov.io/bash)

cd ../frontend
npm run test