def portfolio_analysis(iter,days,paths,tickers,alo):
    
    import MC_funcs
    import numpy

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
        params = [form_p(sim[1]),form_p(sim[2])]
        print(paramstr, params)
        port += sim[0]

    minimum = form_b(min(port))
    maximum = form_b(max(port))
    mean = sum(port)/paths
    pgrowth = form_p(abs(initsum - mean)/mean)

    s1 = 'Minimum of {}, Maximum of {}'.format(minimum,maximum)
    s2 = 'Initial Value: ${} , Average Value: ${}'.format(initsum,form_b(mean))
    s3 = 'Growth: {}'.format(pgrowth)
    
    return port, initsum, s1, s2, s3
