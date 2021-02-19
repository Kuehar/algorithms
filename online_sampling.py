# Assumption: there are at least k elements in the stream

def online_sampling(stream,k):
    # Stores the first k elements
    running_sample = list(itertools.islice(stream,k))

    # Have read the first k elements.
    num_seen_so_far = k
    for i in stream:
        num_seen_so_far = k
        # Generate a random number in [0,num_seen_so_far-1], and if this number is in [0,k-1],
        # we replace that element from the sample with x.
        index_to_replace = random.randrange(num_seen_so_far)
        if index_to_replace < k:
            running_sample[index_to_replace] = x
    return running_sample    