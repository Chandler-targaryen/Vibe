import { Button, Typography } from "@mui/material";
import AuthCard from "../components/AuthCard";
import TextFieldStyled from "../components/TextFieldStyled";
import logo from "../assets/logo.png";

export default function Login() {
  return (
    <AuthCard>
      <img src={logo} style={{ width: 120, marginBottom: 20 }} />

      <Typography variant="h5" sx={{ fontWeight: 700, mb: 2 }}>
        Login
      </Typography>

      <TextFieldStyled label="Email" />
      <TextFieldStyled label="Password" type="password" />

      <Button
        fullWidth
        variant="contained"
        sx={{ mt: 1, mb: 2, bgcolor: "#000000" }}
      >
        Login
      </Button>

      <Typography variant="body2" sx={{ textAlign: "center" }}>
        <a href="/forgot-password" style={{ color: "#000" }}>Forgot Password?</a>
      </Typography>

      <Typography variant="body2" sx={{ textAlign: "center", mt: 1 }}>
        <a href="/signup" style={{ color: "#000" }}>Create an account</a>
      </Typography>
    </AuthCard>
  );
}