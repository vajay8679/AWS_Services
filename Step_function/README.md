# Step Function

https://www.youtube.com/watch?v=ge6Dm2HYG1E

https://medium.com/@saurabh.garg013/an-aws-step-function-capability-is-a-serverless-work-process-administration-that-can-organize-6fd36de0f5b5

we invoke lambda function with the help of step function

in lambad function trigger json
1st lambda

ex. {"time":4}

2nd lambda

ex. {"place":"office"}


1st lambda function ka output will work as input for 2nd lambda function


now create step function -> invoke lambda -> choose lambda function1 -> then next -> next -> create role -> create function 
                         -> execute function -> in json -> {"time":4} -> start exectution -> 

                         then edit state machine -> workflow studio -> lambda invoke -> 
                         choose lambda function2 -> apply and exit -> save -> save anyway -> start execution -> in josn {"time":4}
                         -> start execution and check both function


create new step function -> with type - choice with json 