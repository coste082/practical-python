class FormatError(Exception):
    pass

def create_formatter(fmt):
    formats = {'txt':TextTableFormatter(),
            'csv':CSVTableFormatter(),
            'html':HTMLTableFormatter()}
    try:
        return formats[fmt]
    except:
        raise FormatError('Unknown format: {}'.format(fmt))


class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headers
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self,headers):
        '''Emit the table headings.'''
        for i in headers:
            print('{:>12s}'.format(i),end=' ')
        print()
        print(('-'*12 + ' ')*len(headers))

    def row(self,rowdata):
        for r in rowdata:
            if isinstance(r,str):
                print('{:>12s}'.format(r),end = ' ')
            elif isinstance(r,int):
                print('{:>12d}'.format(r),end = ' ')
            elif isinstance(r,float):
                print('{:>12.2f}'.format(r),end = ' ')
        print('')

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join([str(i) for i in rowdata]))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>',end='')
        for i in headers:
            print('<th>{}</th>'.format(i),end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>',end='')
        for i in rowdata:
            print('<td>{}</td>'.format(str(i)),end='')
        print('</tr>')

