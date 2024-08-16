import { SignJWT, jwtVerify } from 'jose'

const key = ''

const auth = {
  user: null,
  tokens: null,
  sessionCookie: null,

  encrypt: async () => { },

  decrypt: async () => { },

  verifySession: async () => { },

  createSession: async () => { },

  deleteSession: async () => { },

  getUser: async () => { },

  getSession: async () => { },
}


export default auth
