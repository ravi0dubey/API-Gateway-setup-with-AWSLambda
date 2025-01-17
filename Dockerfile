FROM public.ecr.aws/lambda/python:3.12
COPY requirements.txt ${LAMBDA_TASK_ROOT}
COPY . ${LAMBDA_TASK_ROOT}
RUN pip install --no-cache-dir -r requirements.txt
COPY lambda_main.py ${LAMBDA_TASK_ROOT}
CMD ["lambda_main.handler"]
