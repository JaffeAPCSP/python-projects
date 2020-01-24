def checkArguments(sys, testValueCount):
  if (len(sys.argv) < testValueCount+1):
    print('*** Not enough test values - '+str(testValueCount)+' test value expected ***')
    exit()
  else:
    print("\n\n")
  return

