chcp 65001 > NUL
call conda create --name tmp python=3.9
call conda activate tmp
pip install flask
pip install opencv-python
pip install requests
call conda deactivate
rem call conda remove -n tmp --all
pause