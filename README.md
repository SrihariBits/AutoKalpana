# AutoKalpana

Plan
+ Input unsegmented dataset
+ Partition that into parts of 32 or 64 consecutive characters
+ Segment each of the parts based on knowledge based rules and also count number of occurances of each subsegment
+ Assign priority to segments based on these values
+ Consider internal patterns as a complete 
(Optional steps here)
+ Make a document segment matrix
+ Pass through topic modelling with LDA and group segments per topic
(Continuing with mandatory steps)
+ Use a dynamic programming algorithm to partition any given input string into maximum number of known segments from knowledge base
+ Make a vector to show implication of each segment following the prior k segments
+ Pass this to LSTM
+ Generate new segments based on output pattern formats
(Optional steps after this)
+ Compare grouping by topic model with knowledge based grouping
+ Make a GAN (Generative adverserial network) to train discriminator on segmented data and generator through random distribution