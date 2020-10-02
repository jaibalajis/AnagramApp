import React from "react";
import { Grid, Typography, TextField, Button, Paper} from "@material-ui/core";
import { withStyles } from '@material-ui/core/styles';
import axios from 'axios';
import ColorTable from '../components/ColorTable'

// Load the .env file if it exists
require("dotenv").config();

const useStyles = (theme) => ({
    grid:{
        padding: 20
    },
    textfield:{
        border:10,
        marginLeft:20,
        paddingTop:20,
        paddingRight:20,
        textAlign:"center"
    },
    buttonCenter:{
        textAlign:"center",
        padding:40
    },
    heading:{
        padding:40
    }
})

class Anagrams extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            word1: "",
            word2: "",
            popularAnagramsList: [],
            resultString:""
        };
    };

    checkAnagrams=()=>{

        const url=process.env["REACT_APP_BACKEND_URL"]
        const params = {
            word1: this.state.word1,
            word2: this.state.word2
        }
        console.log("url", url, "params:",params)
        axios.get(url,{params}).then((result) =>{
            console.log("Response:",result.data)
            if (result.data.isAnagram){
                if (result.data.isAnagram ==="true"){
                    this.setState({resultString: "Nice! These are valid Anagrams"})
                } else {
                    this.setState({resultString: "Sorry, these are not Anagrams!"})
                }
                if (result.data.popularAnagramsList) {
                    this.setState({popularAnagramsList: result.data.popularAnagramsList})
                }
            }
        });
    }

    handleInput1 = event => {
        this.setState({ word1: event.target.value });
    };
    handleInput2 = event => {
        this.setState({ word2: event.target.value });
    };

    render() {
        const { classes } = this.props;
        const headingDict = {
            word1: "Word 1",
            word2: "Word 2",
            count: "Requested Count"
        }
        return (
            <Grid container direction="column" justify="space-evenly">
                <Grid item>
                    {" "}
                </Grid>
                <Grid container>
                    <Grid item sm={12}>
                        <Typography className={classes.heading} variant="h3" align="center">
                            Anagram Check
                        </Typography>
                    </Grid>
                </Grid>
                <Grid container justify= "center" spacing={3} >
                    <Grid item sm={1}/>
                    <Grid item sm={5}>
                        <Typography variant="h5" align="center">
                                Enter words or phrases to check
                        </Typography>
                        <Paper className={classes.grid} elevation={2}>
                            
                            <Grid className={classes.textfield} item>
                                    <TextField className={classes.textfield} required id="word1" label="Any phrase" onChange={this.handleInput1}/>
                                    <TextField className={classes.textfield} required id="word2" label="Another phrase" onChange={this.handleInput2}/>
                            </Grid>
                            <Grid item>
                                <div className={classes.buttonCenter}>
                                    <Button variant="contained" color="primary" onClick={this.checkAnagrams}>
                                        Check!
                                    </Button>
                                </div>
                            </Grid>
                            <Grid item>
                                <Typography align="center" variant="body1">{this.state.resultString}</Typography>
                            </Grid>
                        </Paper>
                    </Grid>
                    <Grid item sm={5}>
                        <Typography variant="h5" align="center">
                            Top 10 most requested Anagrams
                        </Typography>
                        <Grid item>
                            <ColorTable headingDict={headingDict} popularAnagramsList={this.state.popularAnagramsList}/>
                        </Grid>
                    </Grid>
                    <Grid item sm={1}/>
                </Grid>
                
            </Grid>
        );
    }
}

export default withStyles(useStyles )(Anagrams);