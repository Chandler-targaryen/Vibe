import { TextField } from "@mui/material";

export default function TextFieldStyled(props) {
  return (
    <TextField
      fullWidth
      variant="outlined"
      sx={{
        marginBottom: 2,
        "& .MuiOutlinedInput-root": {
          borderRadius: 2
        }
      }}
      {...props}
    />
  );
}