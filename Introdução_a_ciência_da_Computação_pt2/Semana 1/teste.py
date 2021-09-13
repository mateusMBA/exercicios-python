import unittest
import io
import sys
from module_dimensoes import dimensoes

class TestDimensoes( unittest.TestCase ):
    capturedOutput = None
    def setUp ( self ):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput


    
    def test_dimensoes_linha_maior_coluna( self ):
        minha_matriz = [ [ 1 ], [ 2 ], [ 3 ] ]
        expected_dim = "3X1\n"
        
        dimensoes( minha_matriz )
        dim = self.capturedOutput.getvalue()

        self.assertEqual( dim, expected_dim )

    
    def test_dimensoes_coluna_maior_linha( self ):
        minha_matriz = [ [ 1, 2, 3 ], [ 4 , 5, 6 ] ]
        expected_dim = "2X3\n"
        
        dimensoes( minha_matriz )
        dim = self.capturedOutput.getvalue()
        
        self.assertEqual( dim, expected_dim )


if __name__ == "__main__":
    unittest.main()
