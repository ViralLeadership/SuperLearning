x=5
if ( x <= 3 ) { 
  show('small') 
} else { show('big')
}

for ( countDown in 1000:1 ) {
  show(countDown)
}

for ( note in c('do', 're', 'mi', 'fa', 'so', 'la', 'mi', 'do')) {
  show(note)
}

startTime = proc.time()
for ( countDown in 10000:1 ) {
  show(countDown)
}
stopTime = proc.time()
elapsedTime3 = stopTime - startTime
show(elapsedTime3)
show(elapsedTime2)
show(elapsedTime)
show(elapsedTime - elapsedTime2)
show(elapsedTime - elapsedTime3)
show(elapsedTime2 - elapsedTime3)

source('DBDA2E-utilities.R')
