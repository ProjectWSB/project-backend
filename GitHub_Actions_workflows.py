name: workflow
on: [push]
jobs:
  helloworld:
    runs-on: ubuntu-latest
    steps:
    - name: workflow
      run:
        python -c "print('Hello, World!')"
