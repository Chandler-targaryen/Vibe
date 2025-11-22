import { Button, Typography } from "@mui/material";
import AuthCard from "../components/AuthCard";
import TextFieldStyled from "../components/TextFieldStyled";
import logo from "../assets/logo.png";

export default function Signup() {
  return (
    <AuthCard>
      <img src={logo} style={{ width: 120, marginBottom: 20 }} />

      <Typography variant="h5" sx={{ fontWeight: 700, mb: 2 }}>
        Create Account
      </Typography>

      <TextFieldStyled label="Full Name" />
      <TextFieldStyled label="Email" />
      <TextFieldStyled label="Password" type="password" />

      <Button
        fullWidth
        variant="contained"
        sx={{ mt: 1, mb: 2, bgcolor: "#000000" }}
      >
        Sign Up
      </Button>

      <Typography variant="body2" sx={{ textAlign: "center" }}>
        <a href="/login" style={{ color: "#000" }}>Already have an account?</a>
      </Typography>
    </AuthCard>
  );
}