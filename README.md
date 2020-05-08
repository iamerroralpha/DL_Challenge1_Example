# DL_Challenge1_Example
Example repository for the delivery.

## What is this?

This repo has everything that is needed to evaluate models using h5 files saved from a keras model, according to the framework built by [Emilio](https://github.com/efferreiram/) and [Jacob](https://github.com/edjacob25).

## What should you change?

I built this repo with my own necesities, but it can be used by anyone who is also working with keras. in order for it to work, you should

1. Make sure that you add your own models 1 to 6 in the Models folder (for the example I put only 5 for some reason, but there must be 6).
1. Pur the real and spoof images ""from the TEST set"" in the "/Test_Data_Raw/real" or in the "/Test_Data_Raw/spoof". If you want to structure your images or videos in any other form, it should be consistent with the way the Loader (in the main folder) is setup to have access to your media content.
1. Keep the "Test_Files" folder as shown in this repo, as the content of this folder is necesary to proper call the files within the media (Test_Data_Raw) folder

### Important note for the evaluators: if you are running the evaluate() function in an evnironment running a version of  Python 3.6 or earlier (such as Google Colab), you will need to change the functions perf_counter_ns() to perf_counter() in line 38 and 31 in the Evaluator.py file. as the perf_counter_ns() is new in the built in [time library] (https://docs.python.org/3/library/time.html) @ Python 3.7.  
