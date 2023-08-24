import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

data class UserCredentials(val username: String, val password: String)

data class ApiResponse(val message: String)

interface ApiInterface {
    @POST("api/signin")
    fun signIn(@Body credentials: UserCredentials): Call<ApiResponse>
}
