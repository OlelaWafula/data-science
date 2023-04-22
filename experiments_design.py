import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Design of Experiments
"""
*Experiments generally aim to answer a question of the form: What is the effect of the treatment on the response?
*Treatment refers to the explanatory/independent variable and Response refers to the response/dependent variable. e.g.
        What is the effect of advertising on the number of products purchased. 
            . Treatment = advertisement
            . Response - Number of products purchased. 
"""

# Controlled Experiments 
"""
*Participants are randomly assigned to either treatment group or control group. Where the treatment group receives the treatment and the control group does not. e.g. A/B Test.
            . Treatment group sees the advertisement 
            . Control group does not. 

*The groups should be comparable so that causation can be inferred.
*If the groups are not comparable, this could lead to confounding (bias).
            . If the average age of participants (Treatment group) is 25, and the average age of non-participants (control group) is 50, Age is likely to be a confounder if younger people are likely to practice more. This will make the experiment bias towards the treatment.

*The gold standard/ideal experiment will eliminate as much bias as possible by using certain tools:

        i. Randomized controlled trial:
                        - participants are randomly assigned to the treatment or control group and their assignment isn't based on anything other than chance. 
                        - This helps ensure that the groups are comparable.

        ii. Use a Placebo: 
                        - Something that resembles the treatment but has no effect.
                        - This way, the participants will not know which group they're in i.e. treatment or control group. This ensures that the effect of the treatment is due to treatment itself not the idea of getting the treatment. 
                        - It is common in clinical trials that test the effectiveness of the drug. The control group will be given a pill but it is the sugar pill that has minmal effects on the response. 

        iii. Double-blind trial:
                        - The person administering the treatment or running the experiment also does not know whether they are administering the actual treatment or the placebo. 
                        - This protects against the bias in the response as well as the analysis of the results. 

*All these tools narrow down to the same principle:

        IF THERE ARE FEWER OPPORTUNITIES FOR BIAS TO CREEP INTO YOUR EXPERIMENT, THE MORE RELIABLY YOU CAN CONCLUDE WHETHER THE TREATMENT AFFECTS THE RESPONSE. i.e. Conclusion about causation. 

"""

# Observational studies 
"""
*Participants are not randomly assigned to the groups. Instead participants assign themselves usually based on pre-existing characteristics. 

*This is useful for answering questions that are not conducive to controlled experiment. e.g.

        . If you want to study the effect of smoking on cancer you can't 
                    force people to start smoking. 

        . I f you want to study how past purchasing behavior affects    
                    whether someone will buy a product you can't force people to have certain past purchasing behavior. 

*Because assignment isn't random, there is no way to guarantee that the groups will be comparable in every aspect. 

*Observational studies can only establish association, not causation.

        .   The effects of the treatment may be confounded by factors 
                    that got certain people into the control group and others into the treatment group.

        .   There are ways to control for confounders which can help 
                    strengthen the reliability of the conclusions about association. 
"""

# Longitudinal v. Cross-sectional studies
"""

Longitudinal study                      Cross-sectional study

*Same particitipants are followed       *Data is collected from a single
over a period of time to examine         snapshot in time.
the effect of treatment on the 
response. 

           # To investigate the effect of age on height.

    . The same people will have             . Measure heights of people
    their heights recorded at                 of different ages and 
    different points in their                 compare them. However, the
    lives. So the confounding is              results will be    eliminated.                               confounded by birth year
                                              (generation) and lifestyle since it is possible that each generation is getting taller.  

*They are more expensive and            *Cheaper, faster and more 
results take longer.                     conveniet to perform. 
"""

# EXERCISE 

# Study types
"""
*While controlled experiments are ideal, many situations and research questions are not conducive to a controlled experiment. 
*In a controlled experiment, causation can likely be inferred if the control and test groups have similar characteristics and don't have any systematic difference between them. 
*On the other hand, causation cannot usually be inferred from observational studies, whose results are often misinterpreted as a result.

*A company manufactures thermometers, and they want to study the relationship between a thermometer's age and its accuracy. To do this, they take a sample of 100 different thermometers of different ages and test how accurate they are. Is this data longitudinal or cross-sectional? - This is a cross-sectional study since researchers aren't following the same set of thermometers over time and repeatedly measuring their accuracy at different ages.
"""                                                    