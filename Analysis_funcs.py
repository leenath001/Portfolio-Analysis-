def portfolio_analysis(iter,days,paths,tickers,alo):
    
    import MC_funcs
    import numpy
    import statistics

# number formatting
    def form_p(num):
        return f"{num:.2%}"
    def form_b(num):
        return f"{num:.2f}"

# parameters and asset allocation
    initsum = sum(alo)
    port = numpy.zeros(paths)

    for ind1,names in enumerate(tickers):
        alocs = alo[ind1]
        source = "Data/{}.xlsx".format(names)
        paramstr = "{} params :".format(names)
        sim = MC_funcs.asset_sim(iter,days,alocs,paths,source)
        mu = sim[1]
        sig = sim[2]
        params = [form_p(mu),form_p(sig)]
        print(paramstr, params)
        port += sim[0]

    minimum = form_b(min(port))
    maximum = form_b(max(port))
    stdev = form_b(statistics.stdev(port))
    mean = sum(port)/paths
    pgrowth = form_p(abs(initsum - mean)/mean)

    s1 = 'Min : {}, Max : {}, Stdev : {}'.format(minimum,maximum,stdev)
    s2 = 'Initial Value: ${} , Average Value: ${}'.format(initsum,form_b(mean))
    s3 = 'Growth: {}'.format(pgrowth)
    
    return port, initsum, s1, s2, s3