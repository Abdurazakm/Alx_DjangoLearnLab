### Authentication & Permissions
- Authentication: Token-based (`rest_framework.authtoken`)
- To obtain a token, POST username/password to `/api-token-auth/`
- Use `Authorization: Token <your-token>` header for all requests
- Default permissions: `IsAuthenticated`
- BookViewSet requires authenticated users to access CRUD endpoints
