ABC = c('A', 'B', 'C')
rep(ABC, 2)
rep(ABC, times=2)
rep(ABC, times=c(4, 3, 2))
rep(ABC, each=2)
rep(ABC, each=2, length=10)
rep(ABC, each=2, times=3)
rep(ABC, each=2, times=c(1,2,3,1,2,3))
rep(rep(ABC, each=2), times=c(1,2,3,1,2,3))

x = c( 2.718, 3.14, 1.414, 30135)
x[c(2,4)]
x[c(-1, -3)]
x[c(FALSE, TRUE, FALSE, TRUE)]
names(x) = c('e', 'pi', 'sqrt2', 'zipcode')
x[c('pi', 'zipcode')]

x = c('high', 'medium', 'low', 'high', 'medium')
x
xf = factor(x)
xf
as.numeric(xf)

xfo = factor( x, levels = c('low', "medium", 'high'), ordered=TRUE )
xfo
as.numeric(xfo)

x = c('high', 'medium', 'low', 'high', 'medium')
x
xf = factor(x)
xf
as.numeric(xf)
xf = factor(xf, levels=c('low', 'medium', 'high'), ordered=TRUE)
xf
as.numeric(xf)

xfol = factor( x, levels=c('low', 'medium', 'high' ), ordered=TRUE ,
               labels=c('Bottom SES', 'Middle SES', 'Top SES'))
xfol

matrix( 1:6, ncol=3)
matrix( 1:6, nrow=2)
matrix( 1:6, nrow=3)
matrix( 1:6, nrow=2, byrow=TRUE)
matrix( 1:6, nrow=2, 
        dimnames=list( TheRowDimName=c('Row1Name', 'Row2Name'),
                       TheColDimName=c('Col1Name', 'Col2Name', 'Col3Name')))

x = matrix( 1:6, nrow=2, 
            dimnames=list( TheRowDimName=c('Row1Name', 'Row2Name'),
                           TheColDimName=c('Col1Name', 'Col2Name', 'Col3Name')))
x[2,3]
x['Row2Name', 'Col3Name']
x[2, 1:3]
x[2,]
x[,3]