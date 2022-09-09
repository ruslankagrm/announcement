#!/bin/bash
pipenv install
python -m uvicorn main:announcement_api --reload