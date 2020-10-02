import React from 'react';
import { Table, TableHead, TableBody, TableRow, TableCell} from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';


// setting custom table style
const StyledTableCell = withStyles((theme) => ({
    head: {
      backgroundColor: theme.palette.primary.main,
      color: theme.palette.common.white
    },
    body: {
      fontSize: 14
    }
  }))(TableCell);
  
const StyledTableRow = withStyles((theme) => ({
    root: {
        "&:nth-of-type(odd)": {
        backgroundColor: theme.palette.primary.light
        }
    }
}))(TableRow);

export default function ColorTable(props) {
    const headingDict = props.headingDict
    const popularAnagramsList = props.popularAnagramsList
    
    return (
        <Table>
            <TableHead >
                <TableRow>
                    <StyledTableCell align="center">{headingDict.word1}</StyledTableCell>
                    <StyledTableCell align="center">{headingDict.word2}</StyledTableCell>
                    <StyledTableCell align="center">{headingDict.count}</StyledTableCell>
                </TableRow>
            </TableHead>
            <TableBody>
            {popularAnagramsList.map((anagramDict, index) => (
                <StyledTableRow key={index}>
                    <TableCell align="center">{anagramDict.word1}</TableCell>
                    <TableCell align="center">{anagramDict.word2}</TableCell>
                    <TableCell align="center">{anagramDict.count}</TableCell>
                </StyledTableRow>
            ))}
            </TableBody>
        </Table>
    )
}